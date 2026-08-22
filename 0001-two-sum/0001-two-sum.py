class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i = 0
        j = 1
        while True:
            if nums[i] + nums[j] == target:
                return i,j
            else:
                j += 1
            if j == len(nums):
                i += 1
                j = i+1