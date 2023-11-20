const number1 = parseInt(prompt("First number:"));
const number2 = parseInt(prompt("Second number:"));
const number3 = parseInt(prompt("Third number:"));

const tulos = number1 + number2 + number3;
const keski = tulos / 3;

document.querySelector('#tulo').innerHTML = 'Sum of numbers: ' + tulos;
document.querySelector('#keski').innerHTML = 'Avg of numbers: ' + keski;