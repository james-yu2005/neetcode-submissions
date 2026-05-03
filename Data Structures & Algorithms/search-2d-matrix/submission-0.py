class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        l,r = 0,len(matrix)*len(matrix[0])-1
        while l <= r:
            mid = (l+r)//2
            mid_r = mid // cols
            mid_c = mid % cols
            print(matrix[mid_r][mid_c])
            if matrix[mid_r][mid_c] < target:
                l = mid + 1
            elif matrix[mid_r][mid_c] > target:
                r = mid - 1
            else:
                return True
            print(l,r)
        return False