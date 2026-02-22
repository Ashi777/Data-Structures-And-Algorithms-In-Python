class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            freq = [0] * 26  # frequency array for a..z
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                max_freq = max(freq)
                min_freq = min(f for f in freq if f > 0)  # exclude zeros
                res += max_freq - min_freq
        return res

