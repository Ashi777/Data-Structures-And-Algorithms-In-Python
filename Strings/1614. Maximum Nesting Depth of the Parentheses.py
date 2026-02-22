class Solution:
    def maxDepth(self, s: str) -> int:
        count=0; maxCount=0
        for i in s:
            if i=="(":
                count+=1
                maxCount=max(maxCount, count)
            elif i==")":
                count-=1
            else:
                continue
        return maxCount
