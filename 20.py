'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def isvaild(s):
    match_dic  = {
        ')':'(',
        ']':'[',
        '}':'{',
    }
    stack_li = []
    for each in s:
        if each in match_dic.values():
            stack_li.append(each)
        else:
            if len(stack_li) == 0:
                return False
            if stack_li[-1] == match_dic.get(each):
                stack_li.pop()
            else:
                return False
    if len(stack_li) == 0:
        return True
    else:
        return False

print(isvaild("{[]}"))