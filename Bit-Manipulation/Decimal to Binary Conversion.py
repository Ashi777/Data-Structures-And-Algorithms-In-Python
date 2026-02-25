class Solution:
    def convertToBinary(self, n):
        res = ""
        if n == 0: return "0"
        while (n > 0):
            res += str(n % 2)
            n = n // 2
        return res[::-1]


s = Solution()
ans = s.convertToBinary(13)
print(ans)

# TC -> O(log(base2)N)
# SC -> O(log(base2)N)