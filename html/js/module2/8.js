// Write a function called concat(), which receives an array of strings as a parameter.
// The function returns a string formed by concatenating the elements of the array. (2p)
// Example: In a four-item array, there are items Johnny, DeeDee, Joey and Marky.
// The function returns the string JohnnyDeeDeeJoeyMarky.
// Do not use array.join() function
// You can hard code the array, no need for prompt().
// Print the result to HTML document.

let texttoconc = ["Johnny", "DeeDee", "Joey", "Marky"]
var textresult = ""

function concat(array) {
    textresult = texttoconc[0] + texttoconc[1] + texttoconc[2] + texttoconc[3];
}
concat(texttoconc);
document.getElementById("result").innerText = textresult;