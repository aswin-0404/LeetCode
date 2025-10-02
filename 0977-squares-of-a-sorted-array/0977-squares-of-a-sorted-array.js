/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let arr=[]
    for(let i of nums){
    arr.push(i*i)
    }
    let newarr=arr.sort((a,b)=>a-b)
     return newarr
};
