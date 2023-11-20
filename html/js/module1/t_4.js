const name = prompt("Name: ");
let house = parseInt(Math.random() * 4);

if (house != 0) {
    if (house == 1) {
        house = "Slytherin"
    } else if (house == 2) {
        house = "Hufflepuff"
    } else if (house == 3) {
        house = "Ravenclaw"
    }
} else {
    house = "Gryffindor"
}
document.querySelector('#house').innerHTML = name + " you are part of " + house;

