class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = max(weights);
        high = sum(weights)
        while (low <= high):
            mid = (low + high) // 2
            noofdays = self.findDays(weights, mid)
            if (noofdays <= days):
                high = mid - 1
            else:
                low = mid + 1
        return low

    def findDays(self, weights, capacity):
        day = 1;
        load = 0
        for i in range(len(weights)):
            if (weights[i] + load > capacity):
                day += 1
                load = weights[i]
            else:
                load += weights[i]
        return day

# Driver Code
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
sol=Solution()
ans=sol.shipWithinDays(weights, days)
print(ans)

# TC -> O(log(base2)(sum-max+1)) * O(N)
# SC -> O(1)