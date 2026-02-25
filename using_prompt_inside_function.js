// WRONG: function depends on prompt (hard to reuse) [Using prompt() inside function (bad design) ❌ WRONG – full code]

// const buildArray = () => {
//     let arr = [];
//     let n = Number(prompt("Enter number"));

//     for (let i = 0; i <= n; i++) {
//         arr.push(i);
//     }

//     return arr;
// };

// let result = buildArray();
// console.log(result);


//corrected vesion

// CORRECT: pass values as parameters
const buildArray = (n) => {
    let arr = [];

    for (let i = 0; i <= n; i++) {
        arr.push(i);
    }

    return arr;
};

let result = buildArray(5);
console.log(result);