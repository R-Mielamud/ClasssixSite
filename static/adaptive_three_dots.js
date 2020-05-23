document.body.onload = () => {
    const etalonsCollection = document.getElementsByClassName("width-etalon");
    const etalons = [];

    for (const e of etalonsCollection) {
        etalons.push(e);
    }

    delete etalonsCollection;

    const movableCollection = document.getElementsByClassName("movable");
    const movable = [];

    for (const m of movableCollection) {
        movable.push(m);
    }

    delete movableCollection;

    const threeDotsVertical = document.getElementsByClassName("three-dots-vertical")[0];

    let etalonWidth = 0;

    for (const e of etalons) {
        etalonWidth += e.clientWidth;
    }

    const screenWidth = screen.width;

    for (const movE of movable) {
        if (screenWidth - (etalonWidth + movE.clientWidth) <= 0) {
            threeDotsVertical.appendChild(movE);
        }
    }
};