/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    let p=0
    let n=0
    for(m of moves){
        if(m==="U"){
            p++
        };else if(m==="D"){
            p--
        };else if(m==="L"){
            n--
        };else if(m==="R"){
            n++
        };
    };
    if(p===0&& n===0){
        return true
    };else{
        return false
    };
    
};