class Solution:
    def paint(self, A, B, C):
        low = max(C);
        high = sum(C)
        MOD = 10000003
        while (low <= high):
            mid = (low + high) // 2
            possible = self.func(C, mid)
            if (possible > A):
                low = mid + 1
            else:
                high = mid - 1
        return (low * B) % MOD

    def func(self, C, unit):
        countunit = 1;
        sumunit = 0
        for i in range(len(C)):
            if (sumunit + C[i] <= unit):
                sumunit += C[i]
            else:
                countunit += 1
                sumunit = C[i]
        return countunit

# Driver Code
A = 2
B = 5
C = [1, 10]
sol=Solution()
ans=sol.paint(A, B, C)
print(ans)

# TC -> O(N) * O(log(base2)(sum-max+1))
# SC -> O(1)