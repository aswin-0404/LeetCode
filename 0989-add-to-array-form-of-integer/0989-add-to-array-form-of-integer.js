
var addToArrayForm = function (num, k) {
    let red = num.join("")
    let sum = BigInt(red) + BigInt(k)
    let str = sum.toString()
    let arr = []
    for (let i of str) {
        arr.push(Number(i))
    }
    return arr
};