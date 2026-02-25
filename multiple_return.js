// WRONG: function stops at first return[Multiple return statements❌ WRONG – full code]


// function getData(name, age, place) {
//     let arr = [];

//     for (let i = 0; i <= 3; i++) {
//         arr.push(i);
//     }

//     return arr;      // function exits here
//     return name;     // ❌ unreachable code
// }

// let result = getData("konda", 21, "kadapa");
// console.log(result);


// CORRECT: return everything as a single object
function getData(name, age, place) {
    let arr = [];

    for (let i = 0; i <= 3; i++) {
        arr.push(i);
    }

    return {
        name: name,
        age: age,
        place: place,
        numbers: arr
    };
}

let result = getData("konda", 21, "kadapa");
console.log(result);