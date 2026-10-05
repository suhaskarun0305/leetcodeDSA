class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        lb = -1
        ub = -1

        low,high = 0,len(nums)-1

        while low <= high:
            mid = low+(high-low)//2
            if nums[mid] == target:
                lb = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
            
        if lb == -1:
            return [-1,-1]
            
        low,high = 0,len(nums)-1

        while low <= high:
            mid = low+(high-low)//2
            if nums[mid] == target:
                ub = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return [lb,ub]