/**
 * @param {string} moves
 * @return {number}
 */
var furthestDistanceFromOrigin = function(moves) {
    let counter=0
    let dashcounter=0
    for( let i=0;i<moves.length;i++){
        if(moves[i]==="L"){
            counter--
        }else if(moves[i]==="R"){
            counter++
        }else{
            dashcounter++
        }
    }
    if(counter<0){
        return (counter-dashcounter)*-1
    }else if(counter>0){
        return counter+dashcounter
    }else if(counter===0){
        return dashcounter
    }
};