class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if len(bloomDay)<m*k: return -1
        low=min(bloomDay); high=max(bloomDay); ans=float('inf')
        while(low<=high):
            mid=(low+high)//2
            if(self.possible(bloomDay, mid, m, k)==True):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

    def possible(self, bloomDay, day, m, k):
        count=0; bouquets=0
        for i in range(len(bloomDay)):
            if(bloomDay[i]<=day):
                count+=1
            else:
                bouquets+=(count//k)
                count=0
        bouquets+=count//k
        return bouquets>=m

# Driver Code
bloomDay = [1,10,3,10,2]
m = 3
k = 1
sol=Solution()
ans=sol.minDays(bloomDay, m, k)
print(ans)

# TC -> O(N * log(base2)(max-min+1))
# SC -> O(1)