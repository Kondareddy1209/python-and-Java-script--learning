let n={
    name: "konda",
    age : 21,
    place : "Kadapa",
    DOB : 19052005,
}
for (let key in n){
    if (n.place==="Kadapa"){
        console.log("he is True")
        found=true;
        break;
    }else{
        console.log("He is not True")
    }
}