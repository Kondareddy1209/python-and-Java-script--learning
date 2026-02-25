// WRONG: prompt must use ()[prompt without parentheses❌ WRONG – full code]

// const getName = () => {
//     let name = prompt "Enter name"; // ❌ syntax error
//     return name;
// };

// let result = getName();
// console.log(result);


//corrected version

// CORRECT
const getName = () => {
    let name = prompt("Enter name");
    return name;
};

let result = getName();
console.log(result);