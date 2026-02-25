// WRONG: function expects 3 parameters, only 1 is passed[Wrong function arguments count ❌ WRONG – full code]

// const userInfo = (name, age, place) => {
//     return [name, age, place];
// };

// let result = userInfo(prompt("Enter name"));
// console.log(result); // age & place = undefined

//corrected version
// CORRECT: pass all required arguments
const userInfo = (name, age, place) => {
    return [name, age, place];
};

let result = userInfo(
    prompt("Enter name"),
    Number(prompt("Enter age")),
    prompt("Enter place")
);

console.log(result);