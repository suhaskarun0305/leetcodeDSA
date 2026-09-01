class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        strs.sort()
        a = strs[0]
        b = strs[len(strs)-1]

        if len(a) < len(b):
            ind = len(a)
        else:
            ind = len(b)
        
        res = ""

        for i in range(ind):
            if a[i] != b[i]:
                break
            res += a[i]
        
        return res
