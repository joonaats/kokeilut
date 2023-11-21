function lol() {
    const calculation = document.getElementById("operation").value;
    const num1 = parseInt(document.getElementById("num1").value);
    const num2 = parseInt(document.getElementById("num2").value);
    let result = 0
    if (calculation === "add") {
        result = num1 + num2
    }
    else if (calculation === "sub") {
        result = num1 - num2
    }
    else if (calculation === "multi") {
        result = num1 * num2
    }
    else if (calculation === "div") {
        result = num1 / num2
    }
    document.getElementById("result").innerHTML = result.toString();
}