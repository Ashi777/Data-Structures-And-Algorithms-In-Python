import math
class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        res = 0
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                res = (res + count * (count + 1) // 2) % mod
                count = 1  # reset for new character
        # Add the last group
        res = (res + count * (count + 1) // 2) % mod
        return res
