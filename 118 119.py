
# 杨辉三角的第i行有i个数，其中第一个和最后一个数为1，其余为上一行的xx相加

class Solution:
    def generate(self, numRows: int):
        if numRows == 1:
            return [[[1]]]
        li = [[1],[1,1]]
        row = 2
        while row < numRows:
            new_row = [1]
            for i in range(row-1):
                new_row.append(li[-1][i]+li[-1][i+1])
            new_row.append(1)
            li.append(new_row)
            row += 1
        return li

class Solution:
    def getRow(self, rowIndex: int) :
        li = [[1],[1,1]]
        row = 2
        while row < rowIndex+1:
            new_row = [1]
            for i in range(row-1):
                new_row.append(li[-1][i]+li[-1][i+1])
            new_row.append(1)
            li.append(new_row)
            row += 1
        return li[rowIndex]