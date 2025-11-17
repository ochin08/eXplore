

function validateLogin() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMsg = document.getElementById('error-msg');
    const loginBox = document.getElementById('login-box');

    if (username === "admin" && password === "1234") {
        alert("Login successful!");
    } else {
        errorMsg.style.display = "block";
        loginBox.classList.add("shake");
        setTimeout(() => loginBox.classList.remove("shake"), 300);
    }
}
