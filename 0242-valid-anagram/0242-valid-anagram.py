class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        

        dict1 = {}
        dict2 = {}

        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for j in t:
            if j in dict2:
                dict2[j] += 1
            else:
                dict2[j] = 1

        for i in s:
            if dict1.get(i,0) != dict2.get(i,0):
                return False
        return True