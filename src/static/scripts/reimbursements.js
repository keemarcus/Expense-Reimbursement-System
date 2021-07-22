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
        }

        // use fetch to get all the reimbursements for that user
        url = "http://localhost:5000/users/" + user_id + "/reimbursements"
        response = await fetch(url)
        let reimbursements = await response.json()

        // get our table element
        let table = document.getElementById('reimbursement table')

        // set up a new table row for each reimbursement
        for (reimbursement in reimbursements) {
            let reimbursement_info = reimbursements[reimbursement]
            let reimbursement_id = reimbursement_info['_reimbursement_id']
            let reimbursement_amount = reimbursement_info['_amount']
            let reimbursement_reason = reimbursement_info['_reason']
            let date_created = new Date(reimbursement_info['_date_created']).toLocaleString('en-US', { dateStyle: 'medium', timeStyle: 'short' })
            let reimbursement_status = reimbursement_info['_status']

            // create new table row
            let row = table.insertRow(0)
            let id_cell = row.insertCell(0)
            let amount_cell = row.insertCell(1)
            let reason_cell = row.insertCell(2)
            let date_cell = row.insertCell(3)
            let status_cell = row.insertCell(4)
            let action_cell = row.insertCell(5)
            id_cell.innerText = reimbursement_id
            amount_cell.innerText = reimbursement_amount
            reason_cell.innerText = reimbursement_reason
            reason_cell.id = "reason-" + (reimbursements.size - table.rows.length)
            date_cell.innerText = date_created
            status_cell.innerText = reimbursement_status
            let btn = document.createElement("button")
            action_cell.appendChild(btn)
            btn.innerText = 'edit'
            btn.onclick = () => {
                let row = btn.parentElement.parentElement
                let form_row = document.getElementById('form_row').cloneNode(true)
                form_row.id = 'edit_row'
                let reimbursement_id = row.cells[0].innerText
                let reimbursement_amount = row.cells[1].innerText.replace('$', '')
                let reimbursement_reason = row.cells[2].innerText
                let edit_form = form_row.querySelector('form')
                edit_form.id = 'edit_form'
                edit_form.action = 'http://localhost:5000/reimbursements/' + reimbursement_id

                row.replaceWith(form_row)
                let edit_row = document.getElementById('edit_row')
                edit_row.cells[0].innerText = reimbursement_id
                let form_amount = edit_row.cells[1].querySelector('input')
                form_amount.id = 'edit_amount'
                form_amount.value = reimbursement_amount
                form_amount.setAttribute('form', 'edit_form')
                let form_reason = edit_row.cells[2].querySelector('input')
                form_reason.id = 'edit_reason'
                form_reason.value = reimbursement_reason
                form_reason.setAttribute('form', 'edit_form')
                let submit_btn = edit_row.cells[5].querySelector('input')
                submit_btn.id = 'edit_submit_button'
                submit_btn.setAttribute('form', 'edit_form')
                let cancel_cell = edit_row.cells[4]
                cancel_btn = document.createElement('button')
                cancel_btn.innerText = 'Cancel'
                cancel_btn.onclick = () => {
                    edit_row.replaceWith(row)
                }
                cancel_cell.appendChild(cancel_btn)
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
