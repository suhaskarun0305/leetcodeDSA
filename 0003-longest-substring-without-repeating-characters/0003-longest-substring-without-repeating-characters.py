class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        dic = {}

        max1 = 0
        i = 0
        j = 0
        count = 0

        while j < len(s):
            if s[j] not in dic:
                dic[s[j]] = j
                count += 1
            else:
                i = max(i, dic[s[j]] + 1)
                count = j - i + 1
                dic[s[j]] = j

            if max1 < count:
                max1 = count

            j += 1

        return max1