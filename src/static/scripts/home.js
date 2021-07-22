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

        // set up the login form
        let login = document.getElementById("login")
        login.hidden = false
    }
    else {
        // set up navigation bar
        let reimbursements_button = document.getElementById('reimbursements')
        reimbursements_button.hidden = false
        logout_button = document.getElementById('logout')
        logout_button.onclick = logout

        // set up the reimbursement form
        let login = document.getElementById("request")
        login.hidden = false

        // check to see if the user has manager privileges
        url = "http://localhost:5000/session/is_manager"
        response = await fetch(url)
        let is_manager = await response.text()

        if (is_manager === 'True') {
            // add manager options to navigation bar
            let reviews_button = document.getElementById('reviews')
            reviews_button.hidden = false
            let pending_button = document.getElementById('pending')
            pending_button.hidden = false
            let past_button = document.getElementById('past reimbursements')
            past_button.hidden = false
            let stats_button = document.getElementById('stats')
            stats_button.hidden = false
        }
    }
}

async function logout() {
    console.log('clicked')
    url = "http://localhost:5000/users/logout"
    await fetch(url, { method: 'POST' })
}