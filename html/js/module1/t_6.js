
function calculateSquareRoot() {
    var shouldCalculate = confirm("Should I calculate the square root?");

    if (shouldCalculate) {
        var userInput = prompt("Enter a number:");

        var number = parseFloat(userInput);

        if (!isNaN(number)) {
            if (number < 0) {
                document.getElementById("result").innerHTML = "The square root of a negative number is not defined.";
            } else {
                var squareRoot = Math.sqrt(number);
                document.getElementById("result").innerHTML = "The square root is: " + squareRoot;
            }
        } else {
            document.getElementById("result").innerHTML = "Please enter a valid number.";
        }
    } else {
        document.getElementById("result").innerHTML = "The square root is not calculated.";
    }
}
calculateSquareRoot();