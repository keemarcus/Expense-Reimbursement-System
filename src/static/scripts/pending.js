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
            // use fetch to get all the pending reviews
            url = "http://localhost:5000/reviews/pending"
            response = await fetch(url)
            let reviews = await response.json()
            
            let reviews_button = document.getElementById('reviews')
            reviews_button.hidden = false
            let pending_button = document.getElementById('pending')
            pending_button.hidden = false
            let past_button = document.getElementById('past reimbursements')
            past_button.hidden = false
            let stats_button = document.getElementById('stats')
            stats_button.hidden = false

            // get our table element
            let table = document.getElementById('pending table')

            // fetch the info and set up a new table row for each pending review
            for (review in reviews) {
                let review_info = reviews[review]
                let reimbursement_id = review_info['_reimbursement_id']
                let reimbursement_amount = review_info['_amount']
                let reimbursement_reason = review_info['_reason']
                let employee_id = review_info['_employee_id']

                if (employee_id != user_id) {
                    // create new table row
                    let row = document.getElementById('template row').cloneNode(true)
                    row.id = 'row-' + reimbursement_id
                    row.hidden = false
                    table.appendChild(row)
                    let id_cell = row.cells[0]
                    let employee_cell = row.cells[1]
                    let amount_cell = row.cells[2]
                    let reason_cell = row.cells[3]

                    // insert the review info
                    id_cell.innerText = reimbursement_id
                    employee_cell.innerText = employee_id
                    amount_cell.innerText = reimbursement_amount
                    reason_cell.innerText = reimbursement_reason

                    // set up the form
                    let form = row.querySelector('form')
                    form.id = form.id + reimbursement_id
                    form.action = form.action + reimbursement_id
                    let form_comments = row.cells[4].querySelector('input')
                    form_comments.id = form_comments.id + reimbursement_id
                    form_comments.setAttribute('form', 'form-' + reimbursement_id)
                    let form_result = row.cells[5].querySelector('select')
                    form_result.id = form_result.id + reimbursement_id
                    form_result.setAttribute('form', 'form-' + reimbursement_id)
                    let form_submit = row.cells[6].querySelector('input')
                    form_submit.setAttribute('form', 'form-' + reimbursement_id)
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
