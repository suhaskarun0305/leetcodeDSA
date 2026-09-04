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
        
        max1 = 1
        i = 0
        j = 1
        count = 1

        while j < len(s):
            if s[j] not in s[i:j]:
                j += 1
                count += 1
                if max1 < count:
                    max1 = count
            else:
                if s[j-1] != s[j]:
                    i = j-1
                    while s[i] != s[j]:
                        i -= 1
                    i += 1
                    j += 1
                    count = j-i

                    continue
                count = 1
                i = j
                j += 1
        return max1