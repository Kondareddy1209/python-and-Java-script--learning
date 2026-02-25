// WRONG: for...in gives index, not value[for...in used instead of for...of❌ WRONG]

// let k = ["hello"];
// for (let i in k) {
//     if (i.length > 5) { // i is "0"
//         console.log("Not valid");
//     }
// }


//corrected version
// CORRECT: for...of gives actual value
let k = ["hello"];
for (let i of k) {
    if (i.length > 5) {
        console.log("Not valid");
    }
}