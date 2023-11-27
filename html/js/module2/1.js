let value = 0
let numerot = []
for (let i = 0; i < 5; i++) {
    value = parseInt(prompt("Input number: "))
    numerot.push(value)

}

function reverse(array){
    var output = [];
    for (var i = 0, len= array.length; i< len; i++){
        output.push(array.pop());
    }

    return output;
}
console.log(reverse(numerot));