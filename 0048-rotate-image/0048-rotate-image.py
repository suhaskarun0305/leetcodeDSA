class Solution(object):
    def rotate(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(m)):
            for j in range(i+1,len(m[i])):
                if i == j:
                    continue
                temp = m[i][j]
                m[i][j] = m[j][i]
                m[j][i] = temp
        
        for i in m:
            a = 0
            b = len(i)-1
            while a < b:
                temp = i[a]
                i[a] = i[b]
                i[b] = temp
                a += 1
                b -= 1

        