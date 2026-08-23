class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic = {}

        for i in range(len(nums)):
            n = target-nums[i]
            if n in dic:
                return [dic[n],i+1]
            dic[nums[i]] = i+1