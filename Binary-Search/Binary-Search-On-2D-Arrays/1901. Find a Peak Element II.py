class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        n = len(mat);
        m = len(mat[0])
        low = 0;
        high = m - 1
        while (low <= high):
            mid = (low + high) // 2
            maxRowIndex = self.findMaxIndex(mat, n, m, mid)
            left = mat[maxRowIndex][mid - 1] if mid - 1 >= 0 else -1
            right = mat[maxRowIndex][mid + 1] if mid + 1 < m else -1
            if mat[maxRowIndex][mid] > left and mat[maxRowIndex][mid] > right:
                return [maxRowIndex, mid]
            elif (mat[maxRowIndex][mid] < left):
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]

    def findMaxIndex(self, mat, n, m, col):
        maxValue = -1
        index = -1
        for i in range(n):
            if (mat[i][col] > maxValue):
                maxValue = mat[i][col]
                index = i
        return index

# Driver Code
mat = [[1,4],[3,2]]
sol=Solution()
ans=sol.findPeakGrid(mat)
print(ans)

# TC -> O(log(base 2)M * N)
# SC -> O(1)