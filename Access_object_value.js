// WRONG: k is a key string, not an object[Accessing object value incorrectly❌ WRONG]

// let obj = { place: "kadapa" };
// for (let k in obj) {
//     if (k.place === "kadapa") {
//         console.log("He is from kadapa");
//     }
// }


//corrected version
// CORRECT: access value using obj[key] or obj.place
let obj = { place: "kadapa" };
if (obj.place === "kadapa") {
    console.log("He is from kadapa");
}