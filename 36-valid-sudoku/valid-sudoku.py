class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                current_value=board[r][c]
                if current_value=='.':
                    continue
                if current_value in rows[r] or current_value in cols[c] or current_value in squares[(r//3,c//3)]: 
                    return False
                cols[c].add(current_value)
                rows[r].add(current_value)
                squares[(r // 3,c // 3)].add(current_value)
        return True
        
