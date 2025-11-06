
var findFinalValue = function (nums, original) {
    let i=0;
    while ( i < nums.length) {
        if (nums[i] === original) {
            original = nums[i] * 2
            i = 0
        }else{
            i++
        }
    }
    return original
};