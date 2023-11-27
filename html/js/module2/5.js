let inputNumber;
let arrayNumbers = [];

while (true) {
    inputNumber = parseInt(prompt("Input number"));

    if (!isNaN(inputNumber)) {
        if (arrayNumbers.includes(inputNumber)) {
            alert("Number already inputted");
            break;
        } else {
            arrayNumbers.push(inputNumber);
        }
    } else {
        alert("Invalid input. Please enter a valid number.");
    }
}

arrayNumbers.sort(function (a, b) {
    return a - b;
});

for (let i = 0; i < arrayNumbers.length; i++) {
    console.log(arrayNumbers[i]);
}
