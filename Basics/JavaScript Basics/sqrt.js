function squareRoot(n) {
    for (let index = 0; index <= n; index++) {
        if (index*index === n) {
            console.log("index is square root of n")
            return index; 
        }
        else{
            return index
        }
        
    }
}
squareRoot(16)