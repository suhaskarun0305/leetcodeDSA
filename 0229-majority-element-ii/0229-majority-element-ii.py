class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        res = []

        for i in dic:
            if dic.get(i) > len(nums)//3:
                res.append(i)
        return res