
var getSneakyNumbers = function (nums) {
    let s = [];
    let d = [];
    for (let i of nums) {
        if (s.includes(i)) {
            d.push(i)
        } else {
            s.push(i)
        };
    };
    return d
};