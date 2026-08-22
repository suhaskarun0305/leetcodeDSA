class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        map_s_to_t = {}
        map_t_to_s = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]
            
            if a in map_s_to_t:
                if map_s_to_t[a] != b:
                    return False
            else:
                map_s_to_t[a] = b
            
            if b in map_t_to_s:
                if map_t_to_s[b] != a:
                    return False
            else:
                map_t_to_s[b] = a
        return True