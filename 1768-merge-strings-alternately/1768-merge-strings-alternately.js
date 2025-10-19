
var mergeAlternately = function (word1, word2) {
    let arr = [];
    for (let i = 0; i < word1.length + word2.length; i++) {
        if (arr.length % 2 === 0) {
            arr.push(word1[i])
        };if (arr.length !== 0) {
            arr.push(word2[i])
        };
    };
     return arr.join("")
};