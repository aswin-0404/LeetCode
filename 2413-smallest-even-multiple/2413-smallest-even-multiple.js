/**
 * @param {number} n
 * @return {number}
 */
var smallestEvenMultiple = function(n) {
    if(n%2!==0){
        return 2*n
    }else{
        return n
    }
};