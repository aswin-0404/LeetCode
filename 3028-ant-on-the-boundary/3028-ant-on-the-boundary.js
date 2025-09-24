/**
 * @param {number[]} nums
 * @return {number}
 */
var returnToBoundaryCount = function(nums) {
    let count=0
    let n=0
   for(let i=0;i<=nums.length;i++){
    n=n+nums[i]
    if(n===0){
        count++
    }
   } 
   return count
};