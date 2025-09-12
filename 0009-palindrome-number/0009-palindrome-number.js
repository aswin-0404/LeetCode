/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const result= x.toString().split('').reverse().join('')
    return x.toString()===result
};