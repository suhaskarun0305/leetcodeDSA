class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        i = 0
        j = len(l)-1
        while i<j:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            i += 1
            j -= 1
        return " ".join(l)