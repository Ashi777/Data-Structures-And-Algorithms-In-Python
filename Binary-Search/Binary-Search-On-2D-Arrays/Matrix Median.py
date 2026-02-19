class Solution:
    def findMedian(self, matrix):
        low = float('inf');
        high = float('-inf')
        n = len(matrix);
        m = len(matrix[0])
        for i in range(n):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][m - 1])
        req = (n * m) / 2
        while (low <= high):
            mid = (low + high) // 2
            smallequal = self.countSmallEqual(matrix, n, m, mid)
            if (smallequal <= req):
                low = mid + 1
            else:
                high = mid - 1
        return low

    def countSmallEqual(self, matrix, n, m, x):
        count = 0
        for i in range(n):
            count += self.upperBound(matrix[i], x, m)
        return count

    def upperBound(self, arr, x, n):
        low = 0;
        high = n - 1
        ans = n
        while (low <= high):
            mid = (low + high) // 2
            if (arr[mid] > x):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

# Driver Code
matrix=[ [1, 4, 9], [2, 5, 6], [3, 7, 8] ]
sol=Solution()
ans=sol.findMedian(matrix)
print(ans)

# TC -> O(log(base 2)(10**9) * N * log(base2)M)