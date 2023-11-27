'use strict'
document.addEventListener("DOMContentLoaded", function() {
    let value = 0;
    let nimet = [];
    let parti = parseInt(prompt("Number of people"));

    for (let i = 0; i < parti; i++) {
        value = prompt("Input name: ");
        nimet.push(value);
    }
    
    nimet.sort();

    var resultElement = document.getElementById("result");

    if (resultElement) {
        var ol = document.createElement("ol");

        nimet.forEach(function (name) {
            var li = document.createElement("li");
            li.textContent = name;
            ol.appendChild(li);
        });

        resultElement.appendChild(ol);
    }
});
