
var sortArrayByParity = function(nums) {
    // let a=nums.length 
    // for (let i=0;i<a;i++){
    //     if(nums[i]%2==0){
    //         let a=nums.pop(nums[i])
    //         nums.unshift(a)
    //     }
    // }
    // return nums
     return nums.filter(x => x % 2 === 0).concat(nums.filter(x => x % 2 !== 0));
};