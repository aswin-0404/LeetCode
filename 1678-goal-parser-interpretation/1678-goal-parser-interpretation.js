/**
 * @param {string} command
 * @return {string}
 */
var interpret = function (command) {
    let word = ""
    for (let i = 0; i < command.length; i++) {
        if (command[i] === "G") {
            word += 'G'
        } else if (command[i+1] === ")") {
            word += 'o';
            i++
        } else {
            word += 'al';
            i+=3
        }
    }
    return word
};