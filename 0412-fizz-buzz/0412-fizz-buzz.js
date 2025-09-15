/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function (n) {
    let newarr = []
    for (i = 1; i <= n; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
             newarr.push("FizzBuzz")
        } else if (i % 3 === 0) {
             newarr.push("Fizz")
        } else if (i % 5 === 0) {
             newarr.push("Buzz")
        } else {
             newarr.push(`${i}`)
        }
    }
    return newarr

};