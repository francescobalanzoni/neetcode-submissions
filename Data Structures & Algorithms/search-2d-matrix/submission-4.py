class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        top = 0 
        bottom = len(matrix) - 1 

        while top <= bottom:
            mid_row = (top + bottom) // 2
            if matrix[mid_row][0] > target:
                bottom = mid_row - 1
            elif matrix[mid_row][-1] < target:
                top = mid_row + 1
            else:
                break

        # find column
        left = 0 
        right = len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid_row][mid] > target:
                right = mid - 1
            elif matrix[mid_row][mid] < target:
                left = mid + 1
            else: 
                return True
        
        return False
        