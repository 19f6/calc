let screen = document.getElementById("screen");

function appendToScreen(value) {
    screen.value += value;
}

function clearScreen() {
    screen.value = "";
}

function calculateResult() {
    try {
        screen.value = eval(screen.value);
    } catch (e) {
        screen.value = "Error";
    }
}
