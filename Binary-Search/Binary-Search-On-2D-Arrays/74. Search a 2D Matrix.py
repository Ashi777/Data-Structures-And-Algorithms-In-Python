class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix);
        m = len(matrix[0])
        low = 0;
        high = (n * m) - 1
        while (low <= high):
            mid = (low + high) // 2
            row = mid // m
            col = mid % m
            if (matrix[row][col] == target):
                return True
            elif (matrix[row][col] < target):
                low = mid + 1
            else:
                high = mid - 1
        return False

# Driver Code
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
sol=Solution()
ans=sol.searchMatrix(matrix, target)
print(ans)

# TC -> O(log(base 2)(M*N))