const table = document.getElementById("course-table")
window.addEventListener("load", async ()=>{
    const promise = await fetch("http://localhost:8000/api/v1/course/")
    .then(response=>response.json())
    .then((courses)=>{
        for(let course of courses){
            table.insertAdjacentHTML("beforeend",`<tr><th>Name: ${course.name}</th><th> Credit:${course.credit} Student: ${course.student}</th></tr>`)
        }
    })
})

