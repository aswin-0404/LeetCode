/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) {
    let str=n.toString()
    let arr=str.split("").map(Number)
    let multi=1
    let add=0
    for(let i=0;i<arr.length;i++){
       multi=multi*arr[i]
       add=add+arr[i]
    }
    return multi-add

};