// Write a program that asks the user for numbers until he gives zero.
// The given numbers are printed in the console from the largest to the smallest.
'use strict'

let inputNumbers = []
let inputNumber = 1

while (inputNumber !== 0) {
    inputNumber = parseInt(prompt("Input number"))
        inputNumbers.push(inputNumber)
    inputNumbers.sort(function (b, a) {
        return a - b;
    });
}
for (let i = 0; i < inputNumbers.length; i++) {
    console.log(`Name: ${inputNumbers[i]}`);
}
