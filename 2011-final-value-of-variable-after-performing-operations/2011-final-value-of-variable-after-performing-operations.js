/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let x=0
    for(let i of operations){
        if(i ==="++X"||i==="X++"){
            x++
        }else{
            x--
        }
    }
    return x
};