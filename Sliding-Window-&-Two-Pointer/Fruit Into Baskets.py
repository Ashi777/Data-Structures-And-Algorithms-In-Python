class Solution:
    def totalFruits(self, fruits):
        #your code goes here
        l = 0
        maxlen = 0
        mpp = {}  # dictionary to store fruit counts
        for r in range(len(fruits)):
            mpp[fruits[r]] = mpp.get(fruits[r], 0) + 1  # add fruit at r
            while len(mpp) > 2:  # shrink window if more than 2 types
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]] == 0:
                    mpp.pop(fruits[l])
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen

