
var alku = parseInt(prompt("Enter the start year:"));
var loppu = parseInt(prompt("Enter the end year:"));

var leapYears = [];

for (var year = alku; year <= loppu; year++) {
    if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
        leapYears.push(year);
    }
}

var resultElement = document.getElementById("result");

if (resultElement) {
    var ul = document.createElement("ul");

    leapYears.forEach(function (year) {
        var li = document.createElement("li");
        li.textContent = year;
        ul.appendChild(li);
    });

    resultElement.appendChild(ul);
}
