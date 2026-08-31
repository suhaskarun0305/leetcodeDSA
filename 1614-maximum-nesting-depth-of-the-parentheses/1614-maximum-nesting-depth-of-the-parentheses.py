class Solution(object):
    def maxDepth(self, a):
        """
        :type s: str
        :rtype: int
        """

        m = 0
        count = 0
        for i in a:
            if i == "(":
                count += 1
                if m < count:
                    m = count
            elif i == ")":
                count -= 1
        return m