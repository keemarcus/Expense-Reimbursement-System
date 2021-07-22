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

            // fetch all our stats
            url = "http://localhost:5000/stats"
            response = await fetch(url)
            let stats = await response.json()


            // get our table element
            let table = document.getElementById('stats table')

            // set up a new table row for each reimbursement
            let row = table.insertRow(-1)
            let stat_cell = row.insertCell(0)
            let data_cell = row.insertCell(1)
            stat_cell.innerText = 'Average Expense:'
            data_cell.innerText = stats['Average_Amount']

            row = table.insertRow(-1)
            stat_cell = row.insertCell(0)
            data_cell = row.insertCell(1)
            stat_cell.innerText = 'Largest Single Expense:'
            data_cell.innerText = stats['Highest_Amount']

            row = table.insertRow(-1)
            stat_cell = row.insertCell(0)
            data_cell = row.insertCell(1)
            stat_cell.innerText = 'Employee With Largest Single Expense:'
            data_cell.innerText = stats['Biggest_Spender_Single']

            row = table.insertRow(-1)
            stat_cell = row.insertCell(0)
            data_cell = row.insertCell(1)
            stat_cell.innerText = 'Employee With Largest Total Expenses:'
            data_cell.innerText = stats['Biggest_Spender_Total']
        }
    }
}

// event handler for the logout button
async function logout() {
    console.log('clicked')
    url = "http://localhost:5000/users/logout"
    await fetch(url, { method: 'POST' })
}