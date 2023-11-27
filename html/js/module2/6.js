'use strict'
let rolled = []
let output

function dice() {
    output = Math.floor(Math.random() * 6) + 1;
    rolled.push(output);
}

while (!rolled.includes(6)) {
    dice()
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