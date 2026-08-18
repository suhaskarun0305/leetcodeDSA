class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        flag = 0
        str1 = ""
        for i in s:
            if i == '(':
                flag += 1
            elif i == ')':
                flag -= 1
            if not((flag == 1 and i == '(') or (flag == 0 and i == ')')):
                  str1 += i
        return str1
