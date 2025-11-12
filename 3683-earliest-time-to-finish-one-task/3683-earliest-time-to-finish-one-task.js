
var earliestTime = function (tasks) {
    let out = tasks[0].reduce((a, b) => a + b)
    for (let i = 1; i < tasks.length; i++) {
        let val = tasks[i].reduce((a, b) => a + b)
        if (val < out) {
            out = val
        }
    }
    return out
};