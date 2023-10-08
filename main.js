var inputUsername = document.getElementById("inputUsername")
var inputEmail = document.getElementById("inputEmail")
var inputPass = document.getElementById("inputPass")
var btnSave = document.getElementById("btnSave")
 btnSave.addEventListener("click", function (){
    var user = {
        Name : inputUsername.value,
        Email : inputEmail.value,
        Pass : inputPass.value
    }
    localStorage.setItem("user",JSON.stringify(user))
}) 
