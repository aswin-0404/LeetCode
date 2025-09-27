/**
 * @param {number} x
 * @return {number}
 */
var sumOfTheDigitsOfHarshadNumber = function(x) {
     let str=x.toString()
     let newar=[ Number(str.slice(0, 1)), Number(str.slice(1)) ]
    let val= newar.reduce((a,b)=>a+b)
    if(x%val===0){
        return val
    }else{
        return -1
    }

};