var averageValue = function (nums) {
    let sum = 0
    let count = 0
    for (let i of nums) {
        if (i % 2 === 0 && i % 3 === 0) {
            sum += i
            count++
        }
    }
    return count == 0 ? 0 : Math.floor(sum / count)
};