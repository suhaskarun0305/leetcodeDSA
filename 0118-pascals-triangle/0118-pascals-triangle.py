class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]
        
        res = [[1],[1,1]]

        for i in range(n-2):
            m = []
            for j in range(i+3):
                if j == 0 or j == i+2:
                    m.append(1)
                else:
                    m.append(res[i+1][j-1]+res[i+1][j])
            res.append(m)
        return res

        