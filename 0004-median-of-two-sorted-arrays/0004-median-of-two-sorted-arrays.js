/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let arr=[...nums1,...nums2].sort((a,b)=>a-b)
    if(arr.length%2!==0){
        let val=Math.floor(arr.length/2)
        return arr[val]
    }else{
        let val=arr.length/2
        let evenval=(arr[val]+arr[val-1])/2
        return  evenval
    }
};