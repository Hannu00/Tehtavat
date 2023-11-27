// Write a program that asks for the names of six dogs.
// The program prints dog names to unordered list <ul> in reverse alphabetical order

let dogName = ""
let allDogs = []

for (let i = 0; i <= 5; i++) {
    dogName = prompt("Input dog name");
    allDogs.push(dogName);
}
allDogs.sort()
allDogs.reverse()

var resultElement = document.getElementById("result");

if (resultElement) {
    var ul = document.createElement("ul");

    allDogs.forEach(function (dog) {
        var li = document.createElement("li");
        li.textContent = dog;
        ul.appendChild(li);
    });

    resultElement.appendChild(ul);
}
