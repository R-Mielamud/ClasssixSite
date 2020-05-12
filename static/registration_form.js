let labels = document.getElementsByTagName("label");
let labelsLen = labels.length;
for (let i = 0; i < labelsLen; i++) labels[0].remove();

let username = document.getElementById("id_username");
let password = document.getElementById("id_password");

username.placeholder = "Логін";
password.placeholder = "Пароль";

username.className = "registration-form-input";
password.className = "registration-form-input";