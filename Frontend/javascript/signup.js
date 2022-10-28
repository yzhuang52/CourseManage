const btn = document.getElementById("signup-button")
const form = document.getElementById("signup-form")

function submitForm(data){
    console.log(data)
    form.addEventListener("submit", async (event) => {
        event.preventDefault()
        let promise = await fetch("http://localhost:8000/api/v1/users/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        if(promise.ok){
            location.href = location.href.replace("signup.html", "login.html")
        }
    })
}

btn.addEventListener("click", (event)=>{
    let username = document.getElementById("username").value
    let password = document.getElementById("password").value
    let email = document.getElementById("email").value
    let formdata = {
        "username": username,
        "password": password,
        "email": email
    }
    submitForm(formdata)
    })
