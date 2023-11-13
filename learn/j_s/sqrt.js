function squareroot(n){

    let sq = Math.floor(n / 2);
    let square = sq * sq

    while(square > n){
        sq = Math.floor(sq / 2)
        square = sq * sq
    }

    while(square <= n){
        sq = sq + 1
        square = sq * sq
    }
    return sq -  1
}

let result = squareroot(65  )
console.log(result)