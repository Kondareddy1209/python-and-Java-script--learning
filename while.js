// WRONG: if condition repeats while condition [Redundant condition inside while loop ❌ WRONG ]
// let i = 1;
// while (i < 10) {
//     if (i < 10) { // always true
//         console.log(i, "Konda");
//     }
//     i++;
// }


//corrected version 
// CORRECT: while condition alone is enough
let i = 1;
while (i < 10) {
    console.log(i, "Konda");
    i++;
}