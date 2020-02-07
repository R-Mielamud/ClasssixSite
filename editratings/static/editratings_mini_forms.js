let ratingGaps = document.getElementsByClassName("editratings-form-table-gap");
let ratingGapsLen = ratingGaps.length;
let showingMiniForm = false;

for (let i = 0; i < ratingGapsLen; i++) {
    let gap = ratingGaps[i];

    gap.onclick = () => {
        if (!showingMiniForm) {
            let splitedGapId = gap.id.split("-");
            let miniRatingFormId = `set-rating-mini-form-${splitedGapId[2]}-for-date-${splitedGapId[5]}`;
            let miniRatingForm = document.getElementById(miniRatingFormId);
            miniRatingForm.style.display = "flex";
            let date = splitedGapId[5];
            let day = +splitedGapId[5].split(".")[0];
            miniRatingForm.style.left = `${215 + (+day - 1) * 30}`;
            miniRatingForm.style.top = `${175 + (+splitedGapId[2] - 1) * 15}`;
            gap.style.backgroundColor = "blue";
            showingMiniForm = true;
        }

        return false;
    }
}

let miniForms = document.getElementsByClassName("set-rating-mini-form");
let miniFormsLen = miniForms.length;

for (let i = 0; i < miniFormsLen; i++) {
    let form = miniForms[i];
    let children = form.children;
    let button = children[children.length - 1];
    let gapId = `rating-gap-${button.id.split("-")[5]}-for-date-${button.id.split("-")[8]}`;
    let gap = document.getElementById(gapId);

    button.onclick = () => {
        let inputs = form.children[0].children;
        let input1, input2, input3, input4;
        [input1, input2, input3, input4] = inputs;
        let canSet0F0Bg = input1.value || input2.value || input3.value || input4.value;
        form.style.display = "none";
        gap.style.backgroundColor = canSet0F0Bg ? "#0F0" : "#686";
        showingMiniForm = false;

        if (canSet0F0Bg) {
            gap.value = input1.value || input2.value || input3.value || input4.value;
            gap.title = input1.value + " " + input2.value + " " + input3.value + " " + input4.value;
        } else {
            gap.value = "";
            gap.title = "";
        }

        return false;
    }
}