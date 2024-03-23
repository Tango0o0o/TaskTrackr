var success_btns = document.getElementsByClassName("btn-success");
console.log(success_btns);

function default_color(event) { // stage 1
    event.currentTarget.style.transition = "1s";
    event.currentTarget.style.backgroundColor = "rgb(8, 148, 108)";
};

function on_hover(event) { // stage 2
    event.currentTarget.style.transition = "1s";
    event.currentTarget.style.backgroundColor = "rgb(10, 168, 123)";
};

function onmousedown(event) { // stage 3
    event.currentTarget.style.transition = "0s"; // no transition comin onto the click
    event.currentTarget.style.backgroundColor = "rgb(11, 189, 138)";
};

function onmouseup(event) { // stage 4
    event.currentTarget.style.transition = "0s"; // no transition comin off the click
    event.currentTarget.style.backgroundColor = "rgb(10, 168, 123)";
};

for (const btn of success_btns) {
    btn.addEventListener("mouseout", default_color) // default
    btn.addEventListener("mouseover", on_hover) // about to be clicked
    btn.addEventListener("mousedown", onmousedown) // button is being clicked
    btn.addEventListener("mouseup", onmouseup) // after being clicked but still on it i hope
};