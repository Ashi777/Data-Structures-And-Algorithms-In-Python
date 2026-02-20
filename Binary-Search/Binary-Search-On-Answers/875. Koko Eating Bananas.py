import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1;
        high = max(piles);
        ans = float('inf')
        while (low <= high):
            mid = (low + high) // 2
            totalhrs = self.func(piles, mid)
            if (totalhrs <= h):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def func(self, piles, rate):
        totalhrs = 0
        n = len(piles)
        for i in range(n):
            totalhrs += math.ceil(piles[i] / rate)
        return totalhrs

# Driver Code
piles = [3,6,7,11]
h = 8
sol=Solution()
ans=sol.minEatingSpeed(piles, h)
print(ans)

# TC -> O(log(base2)max element) * O(N)
# SC -> O(1)