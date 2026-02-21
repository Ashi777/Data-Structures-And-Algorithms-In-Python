class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(t)
        n = len(s)
        if m > n:
            return ""

        hash = [0] * 256
        for ch in t:
            hash[ord(ch)] += 1

        l = 0
        r = 0
        count = 0
        minlen = 10**9
        sindex = -1

        while r < n:
            hash[ord(s[r])] -= 1
            if hash[ord(s[r])] >= 0:  # valid character
                count += 1

            while count == m:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    sindex = l

                hash[ord(s[l])] += 1
                if hash[ord(s[l])] > 0:
                    count -= 1
                l += 1

            r += 1

        return "" if sindex == -1 else s[sindex:sindex + minlen]
