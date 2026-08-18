class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        flag = 0
        ans=[]
        for i in s:
            if i == '(':
                flag += 1
            if  flag>1:
                  ans.append(i)
            if i == ')':
                flag -= 1
        return ''.join(ans)
