function login() {

    var username = document.getElementById("username");
    var pass = document.getElementById("password");

    if (username.value == "") {

        alert("Please enter your username!");

    } else if (pass.value  == "") {

        alert("Please enter your password!");

    } else if(username.value == "admin" && pass.value == "admin"){

        window.location.href="dashboard";
    } else if(username.value == "admin" && pass.value == "pass"){
        ;
    } else {

        alert("Please the correct login data!")

    }
}