''''''
'''
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 
“金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)

示例 1:

输入: [5, 4, 3, 2, 1]
输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” 
("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
'''
class Solution:
    def findRelativeRanks(self, score) :
        sort_score = sorted(score,reverse=True)
        dic = {}
        for rank,score1 in enumerate(sort_score):
            dic[score1] = rank+1
        for i in range(len(score)):
            if dic[score[i]] == 1:
                score[i] = "Gold Medal"
            elif dic[score[i]] == 2:
                score[i] = "Silver Medal"
            elif dic[score[i]] == 3:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(dic[score[i]])
        return score

