class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res=[]; i=0
        n=len(intervals)
        #left
        while (i<n and intervals[i][1]<newInterval[0]):
            res.append(intervals[i])
            i+=1
        while(i<n and intervals[i][0]<=newInterval[1]):
            newInterval[0]=min(newInterval[0], intervals[i][0])
            newInterval[1]=max(newInterval[1], intervals[i][1])
            i+=1
        res.append(newInterval)
        while(i<n):
            res.append(intervals[i])
            i+=1
        return res

# Driver Code
intervals = [[1,3],[6,9]]
newInterval = [2,5]
sol=Solution()
ans=sol.insert(intervals, newInterval)
print(ans)

# TC -> O(N)
# SC -> O(N)