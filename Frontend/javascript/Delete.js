const table = document.getElementById("course-table")
const form = document.getElementById("delete-course-form")
const btn = document.getElementById("submit")


function submitForm(data){
    form.addEventListener("submit", async (event)=>{
        event.preventDefault()
        await fetch(`http://localhost:8000/api/v1/course/delete/${data.name}/`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
    })
}


btn.addEventListener("click", (event)=>{
    let name = document.getElementById("course-name").value
    let credit = document.getElementById("course-credit").value
    let student = document.getElementById("student").value
    let formdata = {"name": name, "credit": credit, "student": student}
    submitForm(formdata)
})

window.addEventListener("load", async ()=>{
    const promise = await fetch("http://localhost:8000/api/v1/course/")
    .then(response=>response.json())
    .then((courses)=>{
        for(let course of courses){
            table.insertAdjacentHTML("beforeend",`<tr><th>Name: ${course.name}</th><th> Credit:${course.credit}</th> Student:${course.student}<th></th></tr>`)
        }
    })
})