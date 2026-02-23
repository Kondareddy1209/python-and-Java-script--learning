// function a(x,y){
//     return x+y;
// }

// function b(x,y){
//     return x-y;
// }

// let d=(x,y) =>{
//     return x+y;
// }

// let f = d(4,6);
// console.log(f)
// function c(x,y){
//     return x*y;
// }
// let k=a(5,10)
// console.log(k)



// let m = (a) =>{
//     let c=0
//     for (let char of a){
//         if (char ==='a' || char ==='e' || char==='i' || char==='o' || char==='u'){
//             c++;
//         }
//     }
//     console.log(c)
// }
// let n="saveetha";
// console.log(m(n))


// function a(abc){
//     console.log(abc);
// }
// function b(a){
//     return c;
// }


// let a=[89,90,92,91,79,77,97,99,87,78,98];
// let newArray=a.filter((val)=>{
//     return val>90 ;
// });
 
// console.log(newArray);


let n=Number(prompt("Enter the number"));
let a=[];
for (let  i=1;i<=n;i++){
    a[i+1]=i;
}
console.log(a);
let newArr=a.reduce((val,res)=>{
    return val*res;
})
console.log(newArr);