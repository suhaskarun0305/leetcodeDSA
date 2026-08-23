class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ms = nums[0]
        cs = nums[0]

        for i in range(1,len(nums)):
            cs += nums[i]
            if cs < nums[i]:
                cs = nums[i]
            if ms < cs:
                ms = cs
        return ms
        