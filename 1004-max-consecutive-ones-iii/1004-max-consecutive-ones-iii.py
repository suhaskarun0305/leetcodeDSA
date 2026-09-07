class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        l = r = 0
        count = 0
        max1 = 0

        while r < len(nums):
            if(nums[r]==0):
                count+=1
            while(count>k):
                if(nums[l]==0):
                    count-=1
                l+=1
            r+=1
            max1=max(max1,r-l+1)
        return max1-1
