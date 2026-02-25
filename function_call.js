// WRONG: function is never called[Function NOT called (comma operator mistake)❌ WRONG – full code]
// const getUser = (name, age, place) => {
//     return [name, age, place];
// };

// // This does NOT call the function
// let result = ("konda", 21, "kadapa");

// console.log(result); // prints only "kadapa"


//corrected version
// CORRECT: call the function properly
const getUser = (name, age, place) => {
    return [name, age, place];
};

let result = getUser("konda", 21, "kadapa");

console.log(result);