const dices = parseInt(prompt("Number of dices: "))
var sum = 0

for (var i = 0; i < dices; i++) {
    var dieResult = Math.floor(Math.random() * 6) + 1;

    sum += dieResult;

}
document.querySelector('#result').innerHTML ="sum: " + sum;