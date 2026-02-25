class Solution:
    def convertToDecimal(self, n):
        length = len(n);
        p2 = 1;
        num = 0
        for i in range(length - 1, -1, -1):
            if n[i] == "1":
                num = num + p2
            p2 *= 2
        return num


s = Solution()
ans = s.convertToDecimal("1101")
print(ans)

# TC -> O(length)
# SC -> O(1)
