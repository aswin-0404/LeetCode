/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var getCommon = function(nums1, nums2) {
    if(nums1[nums1.length-1]<nums2[0]){
        return -1
    }
    for(let i of nums1){
        for(let j of nums2){
            if(i===j){
             return i
            }
        }
    }
    return -1
    
};