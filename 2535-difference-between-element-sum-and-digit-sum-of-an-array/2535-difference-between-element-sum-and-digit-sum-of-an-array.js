/**
 * @param {number[]} nums
 * @return {number}
 */
var differenceOfSum = function(nums) {
    let arrsum=nums.reduce((a,b)=>a+b)
    let singlesum=0
    let singarr=nums.join("").split("").map(Number)
    singlesum=singarr.reduce((a,b)=>a+b)
    return arrsum-singlesum
};