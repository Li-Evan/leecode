''''''
# '''
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
# 问总共有多少条不同的路径？
#
# '''
#
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp_li = [[0 for _ in range(n)] for _ in range(m)]
#         for i in range(n):
#             dp_li[0][i] = 1
#         for j in range(m):
#             dp_li[j][0] = 1
#         for i in range(1,m):
#             for j in range(1,n):
#                 dp_li[i][j] = dp_li[i-1][j] + dp_li[i][j-1]
#         return dp_li[m-1][n-1]

'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
'''

# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid) -> int:
#         m = len(obstacleGrid) # 行数
#         n = len(obstacleGrid[0]) # 列数
#         dp_li = [[0 for _ in range(n)] for _ in range(m)]
#         for i in range(m):
#             if obstacleGrid[i][0] == 1:
#                 for front in range(i):
#                     dp_li[front][0] = 1
#                 for later in range(i,n):
#                     dp_li[later][0] = 0
#                 break
#         for j in range(n):
#             if obstacleGrid[0][j] == 1:
#                 for front in range(j):
#                     dp_li[0][front] = 1
#                 for later in range(j,n):
#                     dp_li[0][later] = 0
#                 break
#         for i in range(1,m):
#             for j in range(1,n):
#                 if obstacleGrid[i][j-1] == 1 and obstacleGrid[i-1][j] == 1:
#                     dp_li[i][j] = 0
#                 elif obstacleGrid[i][j] == 1:
#                     dp_li[i][j] = 0
#                 elif obstacleGrid[i][j-1] == 1:
#                     dp_li[i][j] = dp_li[i-1][j]
#                 elif obstacleGrid[i-1][j] == 1:
#                     dp_li[i][j] = dp_li[i][j-1]
#                 else:
#                     dp_li[i][j] = dp_li[i-1][j] + dp_li[i][j-1]
#         return dp_li[m-1][n-1]

'''
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
'''

class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        dp_li = [[0 for _ in range(n)] for _ in range(m)] # 储存到[i][j] 位置的最小路径和

        dp_li[0][0] = grid[0][0]
        for i in range(1,m):
            dp_li[i][0] = grid[i][0] + dp_li[i-1][0]
        for j in range(1,n):
            dp_li[0][j] = dp_li[0][j-1] + grid[0][j]

        for i in range(1,m):
            for j in range(1,n):
                if dp_li[i-1][j] < dp_li[i][j-1]:
                    dp_li[i][j] = dp_li[i-1][j] + grid[i][j]
                else:
                    dp_li[i][j] = dp_li[i][j-1] + grid[i][j]

        return dp_li[m-1][n-1]








