/**
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
    if (n === 0) return 0
    if (n === 1) return 1
    let arr = [0, 1]
    for (let i = 1; i < n; i++) {
        let r = arr[i] + arr[i-1]
        arr.push(r)
    }
    return arr[n]
};