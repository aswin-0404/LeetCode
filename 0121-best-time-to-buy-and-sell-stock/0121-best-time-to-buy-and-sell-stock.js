/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let min=prices[0]
    let profit=0
    for(let i of prices){
        if(i<min){
            min=i
        }else if(i-min>profit){
            profit=i-min
        }
    }
    return profit
};