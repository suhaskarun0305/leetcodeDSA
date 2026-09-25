class Solution(object):
    def maxScore(self, c, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """

        if len(c) == 0 or k == 0:
            return 0

        if k == len(c):
            return sum(c)

        if k == 1:
            return max(c[0],c[len(c)-1])
        
        sum1 = 0
        i = 0
        j = len(c) - k - 1
        x = sum(c)
        a = sum(c[i:j+1])

        while j < len(c):
            if i != 0:
                a += c[j]
                a -= c[i-1]
            sum1 = max(sum1,x-a)
            i += 1
            j +=1

        return sum1

