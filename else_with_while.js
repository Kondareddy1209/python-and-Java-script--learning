// WRONG: while loop cannot have else in JavaScript[else with while (invalid syntax) ❌ WRONG]

// let i = 5;
// while (i < 10) {
//     console.log(i);
// } else {
//     console.log("Out of bounds"); // syntax error
// }

// CORRECT: use if-else outside the loop
let i = 5;
if (i < 10) {
    while (i < 10) {
        console.log(i);
        i++;
    }
} else {
    console.log("Out of bounds");
}