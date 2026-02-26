class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1], reverse=False)
        count=1; lastEndTime=intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0]>=lastEndTime:
                count+=1
                lastEndTime=intervals[i][1]
        return len(intervals)-count

# Driver Code
intervals = [[1,2],[2,3],[3,4],[1,3]]
sol=Solution()
ans=sol.eraseOverlapIntervals(intervals)
print(ans)

# TC -> O(N + NlogN)
# SC -> O(1)