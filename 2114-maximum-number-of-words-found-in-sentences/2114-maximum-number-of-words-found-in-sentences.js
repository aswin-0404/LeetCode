/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    let count=0
    let maxcount=0
    for(let i of sentences){
        for(let j of i){
            if(j===" "){
                count++
            }
        }
        if(maxcount<count){
            maxcount=count
        }
        count=0
    }
    return maxcount+1
};