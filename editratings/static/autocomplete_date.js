let dates = document.getElementsByClassName("editratings-form-date-input");
let datenow = new Date();

let getMonth = datenow => {
    let month = datenow.getMonth() + 1;
    if (month < 10) return "0" + month;
    else return month;
}

let getDay = datenow => {
    let day = datenow.getDate();
    if (day < 10) return "0" + day;
    else return day;
}

let dateFormatted = [datenow.getFullYear(), getMonth(datenow), getDay(datenow)].join("-");
for (let d of dates) d.value = dateFormatted;