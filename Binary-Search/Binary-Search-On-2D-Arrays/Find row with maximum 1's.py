class Solution:
    def rowWithMax1s(self, mat):
        m = len(mat[0])
        countmax = 0;
        index = -1
        for i in range(len(mat)):
            countones = m - self.lowerbound(mat[i], len(mat[0]), 1)
            if (countones > countmax):
                countmax = countones
                index = i
        return index

    def lowerbound(self, arr, n, x):
        low = 0;
        high = n - 1
        ans = n
        while (low <= high):
            mid = (low + high) // 2
            if (arr[mid] >= x):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans

# Driver Code
mat = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]
sol=Solution()
ans=sol.rowWithMax1s(mat)
print(ans)

# TC -> O(Nlog(base 2)M)
# SC -> O(1)