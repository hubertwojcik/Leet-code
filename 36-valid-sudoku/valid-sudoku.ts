function isValidSudoku(board: string[][]): boolean {
    const cols = new Map<number, Set<string>>()
    const rows = new Map<number, Set<string>>()
    const squares = new Map<number, Set<string>>()

    for (let r = 0; r < 9; r++){
        for(let c = 0; c < 9; c++){
            const num = board[r][c]
            if(num === '.') continue

            const squareIndex = Math.floor(r / 3) * 3 + Math.floor(c / 3)

            if(!rows[r]) rows[r] = new Set()
            if(!cols[c]) cols[c] = new Set()
            if(!squares[squareIndex]) squares[squareIndex] = new Set()

            if (rows[r].has(num) || cols[c].has(num) || squares[squareIndex].has(num)){
                return false
            }
            rows[r].add(num)
            cols[c].add(num)
            squares[squareIndex].add(num)
        }
    }
    return true
};