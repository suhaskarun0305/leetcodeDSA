class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans = [0] * len(nums)

        i = 0
        j = 1
        
        for a in nums:
            if a > 0:
                ans[i] = a
                i += 2
            else:
                ans[j] = a
                j += 2
        return ans