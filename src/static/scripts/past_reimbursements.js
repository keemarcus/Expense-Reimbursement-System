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

            // use fetch to get all the reimbursements for that user
            url = "http://localhost:5000/reimbursements/past"
            response = await fetch(url)
            let reimbursements = await response.json()

            // get our table element
            let table = document.getElementById('reimbursement table')

            // set up a new table row for each reimbursement
            for (reimbursement in reimbursements) {
                // retrieve the data about the reimbursement
                let reimbursement_info = reimbursements[reimbursement]
                let reimbursement_id = reimbursement_info['_reimbursement_id']
                let employee_id = reimbursement_info['_employee_id']
                let reimbursement_amount = reimbursement_info['_amount']
                let reimbursement_reason = reimbursement_info['_reason']
                let date_created = new Date(reimbursement_info['_date_created']).toLocaleString('en-US', { dateStyle: 'medium', timeStyle: 'short' })

                // create new table row
                let row = table.insertRow(0)
                let id_cell = row.insertCell(0)
                let employee_cell = row.insertCell(1)
                let amount_cell = row.insertCell(2)
                let reason_cell = row.insertCell(3)
                let date_cell = row.insertCell(4)

                // insert the data into the new row
                id_cell.innerText = reimbursement_id
                employee_cell.innerText = employee_id
                amount_cell.innerText = reimbursement_amount
                reason_cell.innerText = reimbursement_reason
                date_cell.innerText = date_created
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
