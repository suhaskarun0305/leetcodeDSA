class Solution(object):
    def maxProfit(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        i = 0
        j = 1

        while j < len(nums):

            if nums[j] < nums[i]:
                i = j
            else:
                if profit < nums[j] - nums[i]:
                    profit = nums[j] - nums[i]
            j += 1
        return profit