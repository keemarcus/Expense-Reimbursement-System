set_up_page()

async function set_up_page() {
    // use fetch to get the id of the signed in user
    let url = "http://localhost:5000/session/user_id"
    let response = await fetch(url)
    user_id = await response.text()

    if (user_id === 'None') {
        // set up navigation bar
        login_button = document.getElementById('logout')
        login_button.innerText = 'Log In'
        login_button.href = "/login.html"
    }
    else {
        // set up navigation bar
        logout_button = document.getElementById('logout')
        logout_button.onclick = logout

        // check to see if the user has manager privileges
        url = "http://localhost:5000/session/is_manager"
        response = await fetch(url)
        let is_manager = await response.text()

        if (is_manager === 'True') {
            let reviews_button = document.getElementById('reviews')
            reviews_button.hidden = false
            let pending_button = document.getElementById('pending')
            pending_button.hidden = false
            let past_button = document.getElementById('past reimbursements')
            past_button.hidden = false
            let stats_button = document.getElementById('stats')
            stats_button.hidden = false

            // use fetch to get all the reviews for that user
            url = "http://localhost:5000/users/" + user_id + "/reviews"
            response = await fetch(url)
            let reviews = await response.json()

            // get the table element
            let table = document.getElementById('reviews table')

            // fetch the info and set up a new table row for each review
            for (review in reviews) {
                let review_info = reviews[review]
                let reimbursement_id = review_info['_reimbursement_id']
                let review_comments = review_info['_review_comments']
                let review_result = review_info['_status']
                let review_date = new Date(review_info['_date_reviewed']).toLocaleString('en-US', { dateStyle: 'medium', timeStyle: 'short' })
                let reimbursement_amount = review_info['_amount']
                let reimbursement_reason = review_info['_reason']
                let employee_id = review_info['_employee_id']

                // create new table row
                let row = table.insertRow(0)
                let id_cell = row.insertCell(0)
                let employee_cell = row.insertCell(1)
                let amount_cell = row.insertCell(2)
                let reason_cell = row.insertCell(3)
                let comments_cell = row.insertCell(4)
                let result_cell = row.insertCell(5)
                let date_cell = row.insertCell(6)
                let edit_cell = row.insertCell(7)

                // insert the info into the new table row
                id_cell.innerText = reimbursement_id
                employee_cell.innerText = employee_id
                amount_cell.innerText = reimbursement_amount
                reason_cell.innerText = reimbursement_reason
                comments_cell.innerText = review_comments
                result_cell.innerText = review_result
                date_cell.innerText = review_date

                // set up the button elements
                let edit_btn = document.createElement("button")
                edit_btn.innerText = 'Edit'
                edit_btn.id = 'edit-' + reimbursement_id
                edit_cell.appendChild(edit_btn)

                // set up the event handler for the edit button
                edit_btn.onclick = () => {
                    // set up the new row containing the form to edit the review
                    let row = edit_btn.parentElement.parentElement
                    let form_row = document.getElementById('form_row').cloneNode(true)
                    form_row.id = 'edit_row'
                    form_row.hidden = false

                    // copy over the info we need for the new row with the form
                    form_row.cells[7].replaceWith(row.cells[7].cloneNode(true))
                    let reimbursement_id = row.cells[0].innerText
                    let employee_name = row.cells[1].innerText
                    let amount = row.cells[2].innerText
                    let reason = row.cells[3].innerText
                    let comments = row.cells[4].innerText
                    let result = row.cells[5].innerText


                    // set up the form element itself
                    let edit_form = form_row.querySelector('form')
                    edit_form.id = 'edit_form'
                    edit_form.action = edit_form.action + reimbursement_id
                    let form_reimbursement_id = form_row.querySelector('input')
                    form_reimbursement_id.value = reimbursement_id
                    form_reimbursement_id.id = 'edit_id'
                    form_reimbursement_id.setAttribute('form', 'edit_form')

                    // repolace the normal row with the form row
                    row.replaceWith(form_row)

                    // insert the info from the normal row into the form row
                    let edit_row = document.getElementById('edit_row')
                    edit_row.cells[0].innerText = reimbursement_id
                    edit_row.cells[1].innerText = employee_name
                    edit_row.cells[2].innerText = amount
                    edit_row.cells[3].innerText = reason

                    // set up the input elements of the form
                    let form_comments = edit_row.cells[4].querySelector('input')
                    form_comments.id = 'edit_comments'
                    form_comments.value = comments
                    form_comments.setAttribute('form', 'edit_form')
                    let form_result = edit_row.cells[5].querySelector('select')
                    form_result.id = 'edit_result'
                    form_result.querySelector('#' + result).selected = true
                    form_result.setAttribute('form', 'edit_form')
                    let submit_btn = edit_row.cells[6].querySelector('input')
                    submit_btn.id = 'submit_button'
                    submit_btn.setAttribute('form', 'edit_form')

                    // change the edit button to a cancel button to cancel editing
                    cancel_btn = document.createElement('button')
                    cancel_btn.innerText = 'Cancel'
                    cancel_btn.onclick = () => {
                        edit_row.replaceWith(row)
                        edit_btn = row.cells[7].querySelector('#edit-' + reimbursement_id)
                    }
                    edit_btn = edit_row.cells[7].querySelector('#edit-' + reimbursement_id)
                    edit_btn.replaceWith(cancel_btn)

                }
            }
        }
    }
}

// event handler for the logout button
async function logout() {
    console.log('clicked')
    url = "http://localhost:5000/users/logout"
    await fetch(url, { method: 'POST' })
}
