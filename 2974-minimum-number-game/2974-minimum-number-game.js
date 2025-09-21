/**
 * @param {number[]} nums
 * @return {number[]}
 */
var numberGame = function (nums) {
    let arr = []
    let sortarr = nums.sort((a, b) => a - b)
    for (let i = 1; i <= sortarr.length; i+=2) {
        arr.push(sortarr[i],sortarr[i-1])
    }
    return arr
};