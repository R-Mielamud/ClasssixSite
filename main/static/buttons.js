let registrationButton = document.getElementById("registrationButton");
let unregistrationButton = document.getElementById("unregistrationButton");
let registrationFormBg = document.getElementById("registrationFormBg"); 
let registrationFormReset = document.getElementById("registrationFormReset");
let toMainButton = document.getElementById("toMainButton");
let addArticleButton = document.getElementById("addArticleButton");

registrationButton.onclick = () => registrationFormBg.style.display = "flex";
registrationFormReset.onclick = () => registrationFormBg.style.display = "none";
unregistrationButton.onclick = () => window.location.href = "/?unregister=1";
toMainButton.onclick = () => window.location.href = "/";
toDiaryButton.onclick = () => window.location.href = "/diary/";
editRatingsButton.onclick = () => window.location.href = "/editratings/";
addArticleButton.onclick = () => window.location.href = "/add_article/"

if (showedButton) {
    registrationButton.style.display = "none";
    unregistrationButton.style.display = "block";
}