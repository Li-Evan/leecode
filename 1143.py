''''''
'''最长公共子序列'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == '' or text2 == '':
            return 0
        m = len(text1)
        n = len(text2)
        li = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    li[i][j] = li[i-1][j-1] + 1
                else:
                    li[i][j] = max(li[i][j-1],li[i-1][j])
        return li[m][n]