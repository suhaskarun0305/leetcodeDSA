class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ms = nums[0]
        cs = nums[0]

        for i in range(1,len(nums)):
            cs = max(cs+nums[i],nums[i])
            ms = max(ms,cs)
        return ms
        