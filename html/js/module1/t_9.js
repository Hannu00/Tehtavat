'use strict'

const value1 = parseInt(prompt("Input number: "))

function isPrime(num) {
    var sqrtnum = Math.floor(Math.sqrt(num));
    var prime = num !== 1;
    for (var i = 2; i < sqrtnum + 1; i++) { // sqrtnum+1
        if (num % i === 0) {
            prime = false;
            break;
        }
    }
    return prime;
}

if (isPrime(value1) === false) {
    document.getElementById("result").innerText = "Number: " + value1 + " is not prime number"
} else if (isPrime(value1) === true) {
    document.getElementById("result").innerText = "Number: " + value1 + " is prime number"
} else {
    document.getElementById(result).innerText = "Invalid input"
}