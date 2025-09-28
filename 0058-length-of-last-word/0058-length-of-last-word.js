/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let ns=s.trim()
    let arr=ns.split(" ")
    let w=arr[arr.length-1]
    let len=w.length
      return len
};