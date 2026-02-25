// WRONG: k.length is array length, not string length[Checking array length instead of string length❌ WRONG]

// let k = ["123456"];
// for (let i of k) {
//     if (k.length > 5) {
//         console.log("Not valid");
//     }
// }


//corrected version
// CORRECT: check length of each string
let k = ["123456"];
for (let i of k) {
    if (i.length > 5) {
        console.log("Not valid");
    }
}