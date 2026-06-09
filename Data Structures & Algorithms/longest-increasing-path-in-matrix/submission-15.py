class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]

        def dfs(x, y, prevVal):
            if (
                x < 0 or x == rows or
                y < 0 or y == cols or
                matrix[x][y] <= prevVal
            ):
                return 0

            if dp[x][y]:
                return dp[x][y]

            res = 1
            res = max(res, 1 + dfs(x + 1, y, matrix[x][y]))
            res = max(res, 1 + dfs(x - 1, y, matrix[x][y]))
            res = max(res, 1 + dfs(x, y + 1, matrix[x][y]))
            res = max(res, 1 + dfs(x, y - 1, matrix[x][y]))

            dp[x][y] = res
            return res

        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j, -1))

        return ans