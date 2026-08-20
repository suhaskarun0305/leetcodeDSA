class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        num = int(num)
        while num != 0:
            if num%2 != 0:
                return str(num)
            num = num//10
        return ""

