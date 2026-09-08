class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        dic = {}

        r = l = 0
        max1 = 0

        while r < len(fruits):
            if fruits[r] not in dic:
                dic[fruits[r]] = 1
            else:
                dic[fruits[r]] += 1
             
            while len(dic) > 2:
                if dic[fruits[l]] == 1:
                    dic.pop(fruits[l])
                else:
                    dic[fruits[l]] -= 1
                l += 1

            max1 = max(max1,r-l+1)
            r += 1
        return max1
                