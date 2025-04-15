class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top_r, bot_r = 0, rows - 1

        while top_r <= bot_r:
            mid_row = (top_r + bot_r) // 2
            if target > matrix[mid_row][-1]:
                top_r = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot_r = mid_row - 1
            else:
                break
        
        if not (top_r <= bot_r):
            return False
        
        row = (top_r + bot_r) // 2
        left, right = 0, len(matrix[row])

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False