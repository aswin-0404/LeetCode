var isThree = function (n) {
    let num = Math.sqrt(n);
    if(!Number.isInteger(num)) return false;
    if (num <= 1) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false;
    for (let i = 3; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            return false
        }
    }
    return true
};