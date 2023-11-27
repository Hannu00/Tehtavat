'use strict'
let rolled = []
let output
let maxdice = parseInt(prompt("Max dice face number"))

function dice(max) {
    output = Math.floor(Math.random() * max) + 1;
    rolled.push(output);
}

while (!rolled.includes(maxdice)) {
    dice(maxdice)
}
var resultElement = document.getElementById("result");

if (resultElement) {
    var ul = document.createElement("ul")

    rolled.forEach(function (number) {
        var li = document.createElement("li");
        li.textContent = number;
        ul.appendChild(li);
    });
    resultElement.appendChild(ul)
}