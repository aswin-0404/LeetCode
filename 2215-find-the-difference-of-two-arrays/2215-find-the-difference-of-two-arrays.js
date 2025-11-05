
var findDifference = function (nums1, nums2) {
    let news = new Set(nums1)
    let news1 = new Set(nums2)
    let arr1 = [...news].filter(v => !news1.has(v))
    let arr2 = [...news1].filter(v => !news.has(v))
    return [arr1, arr2]
};