/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function (jewels, stones) {
    let count = 0
    for (let i of stones) {
        for (let j of jewels) {
            if (j === i) {
                count++
            }
        }
    }
    return count
};