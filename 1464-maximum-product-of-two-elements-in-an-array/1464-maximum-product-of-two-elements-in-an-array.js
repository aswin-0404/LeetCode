/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let arr=nums.sort((a,b)=>a-b)
    let l=arr.pop()
    let s=arr.pop()
    // console.log(arr)
    return (l-1)*(s-1)
};