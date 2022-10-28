const btn = document.getElementById("login-button")
const form = document.getElementById("login-form")

function submitForm(data){

    form.addEventListener("submit", async (event) => {
        event.preventDefault()
        let auth_token = await fetch("http://localhost:8000/api/v1/token/login/", {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
            },
            body: JSON.stringify(data)
        }).then((Response)=>{
            return Response.json()
        }).then((data)=>{
            localStorage.removeItem("token")
            localStorage.setItem("token", data.auth_token)
        })

    })
}

btn.addEventListener("click", (event)=>{
    let username = document.getElementById("username").value
    let password = document.getElementById("password").value
    let email = document.getElementById("email").value
    let formdata = {"username": username, "password": password, "email": email}
    submitForm(formdata)
    })

window.addEventListener("load", ()=>{
    if(localStorage.getItem("token")){
        location.href = location.href.replace("login.html", "home.html")
    }
})