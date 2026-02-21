class Solution:
    def kDistinctChar(self, s, k):
        # your code goes here
        maxlen = 0
        l = 0
        mpp = {}  # dictionary to count characters

        for r in range(len(s)):
            mpp[s[r]] = mpp.get(s[r], 0) + 1  # add char at r

            while len(mpp) > k:  # shrink window if more than k distinct chars
                mpp[s[l]] -= 1
                if mpp[s[l]] == 0:
                    mpp.pop(s[l])
                l += 1

            maxlen = max(maxlen, r - l + 1)

        return maxlen
