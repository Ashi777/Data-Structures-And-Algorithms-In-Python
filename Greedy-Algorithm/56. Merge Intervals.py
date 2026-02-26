class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n=len(intervals)
        ans=[]
        intervals.sort()
        for i in range(n):
            if not ans or intervals[i][0]>ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1]=max(ans[-1][1], intervals[i][1])
        return ans

# Driver Code
intervals = [[1,3],[2,6],[8,10],[15,18]]
sol=Solution()
ans=sol.merge(intervals)
print(ans)

# TC -> O(N + NlogN)
# SC -> O(N)