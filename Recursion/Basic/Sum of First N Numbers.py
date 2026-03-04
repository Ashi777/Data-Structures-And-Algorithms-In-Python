class Solution:
    def NnumbersSum(self, N):
        if N == 1:
            return 1
        return N + self.NnumbersSum(N - 1)

sol = Solution()
print(sol.NnumbersSum(4))  # Output: 10
print(sol.NnumbersSum(2))