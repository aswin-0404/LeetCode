/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
      let arr= address.replaceAll(".","[.]")
       return arr
}