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
            if  flag>1:
                  str1 += i
            if i == ')':
                flag -= 1
        return str1
