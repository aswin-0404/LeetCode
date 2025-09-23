/**
 * @param {string} text
 * @param {string} brokenLetters
 * @return {number}
 */
var canBeTypedWords = function (text, brokenLetters) {
    let newtext = text.split(" ")
    let count = newtext.length
    for (let i = 0; i < newtext.length; i++) {
        for (l of  brokenLetters) {
            if (newtext[i].includes(l)) {
                count--
                break;
            }
        }
    }

    return count
};