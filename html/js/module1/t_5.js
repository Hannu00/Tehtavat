
function isLeapYear(year) {
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}

function checkLeapYear() {
    var yearInput = prompt("Enter a year:");
    var year = parseInt(yearInput);

    if (!isNaN(year)) {
        var result = isLeapYear(year);
        // Display the result in the HTML document
        document.getElementById("result").innerHTML = "<p>" + year + " is " + (result ? "a leap year." : "not a leap year.") + "</p>";
    } else {
        alert("Please enter a valid number.");
    }
}

window.onload = checkLeapYear;
