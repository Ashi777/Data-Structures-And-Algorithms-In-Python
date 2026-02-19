class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix);
        m = len(matrix[0])
        row = 0;
        col = m - 1
        while (row < n and col >= 0):
            if (matrix[row][col] == target):
                return True
            elif (matrix[row][col] < target):
                row += 1
            else:
                col -= 1
        return False

# Driver Code
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
sol=Solution()
ans=sol.searchMatrix(matrix, target)
print(ans)

# TC -> O(N + M)
# SC -> O(1)