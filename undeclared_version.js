// WRONG: n becomes a global variable[Undeclared variable (n) ❌ WRONG – full code]

// const generateNumbers = () => {
//     let arr = [];
//     n = Number(prompt("Enter number")); // ❌ no let

//     for (let i = 0; i <= n; i++) {
//         arr.push(i);
//     }

//     return arr;
// };

// let result = generateNumbers();
// console.log(result);

// CORRECT: declare variable with let
const generateNumbers = () => {
    let arr = [];
    let n = Number(prompt("Enter number")); // ✅ declared

    for (let i = 0; i <= n; i++) {
        arr.push(i);
    }

    return arr;
};

let result = generateNumbers();
console.log(result);