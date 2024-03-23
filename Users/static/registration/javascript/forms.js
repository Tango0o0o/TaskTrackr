var password_input = document.getElementById("password");
var show_pass_btn = document.getElementById("show-password-button");

function show_password(event) {

    if (password_input.type == "password") {

        password_input.type = "text";
        show_pass_btn.innerHTML = "Hide password"

    } else {

        password_input.type = "password";
        show_pass_btn.innerHTML = "Show password"

    }

};
    
function adjust_button_borders(event) {  //Adjusting the show password button borders


    // Styling borders
    show_pass_btn.style.border = "black solid 1px"
    show_pass_btn.style.borderLeft = "black solid 2px"

    // to fit in with the input
    show_pass_btn.style.borderRadius = "3px"

    // straight left border
    show_pass_btn.style.borderTopLeftRadius = "0px"
    show_pass_btn.style.borderBottomLeftRadius = "0px"

};

function original_button_borders(event) {  // Resetting the show password button borders

    // Resetting borders
    show_pass_btn.style.border = "none";
    show_pass_btn.style.borderLeft = "solid #cccccc 1px";

};

function button_click(event) { // when the button is clicked
    show_pass_btn.style.border = "groove 1px white"
    show_pass_btn.style.borderLeft = "solid #cccccc 1px";
    show_pass_btn.style.backgroundColor = "#fafafa";
};

function button_end_click(event) { // when the button has finished being clicked
    show_pass_btn.style.border = "none";
    show_pass_btn.style.borderLeft = "solid #cccccc 1px";
    show_pass_btn.style.backgroundColor = "white";
};

password_input.addEventListener("focus", adjust_button_borders);
password_input.addEventListener("blur", original_button_borders);

show_pass_btn.addEventListener("click", show_password);

show_pass_btn.addEventListener("mousedown", button_click);
show_pass_btn.addEventListener("mouseup", button_end_click);