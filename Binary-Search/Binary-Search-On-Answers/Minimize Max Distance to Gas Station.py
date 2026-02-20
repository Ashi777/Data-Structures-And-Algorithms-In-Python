class Solution:
    def minimiseMaxDistance(self, arr, k):
        low = 0;
        high = 0
        for i in range(len(arr) - 1):
            high = max(high, arr[i + 1] - arr[i])
        diff = 1e-6
        while (high - low > diff):
            mid = (low + high) / 2.0
            count = self.noOfGasStationsRequired(arr, mid)
            if (count > k):
                low = mid
            else:
                high = mid
        return high

    def noOfGasStationsRequired(self, arr, dist):
        count = 0
        for i in range(1, len(arr)):
            numberInBetween = int((arr[i] - arr[i - 1]) / dist)
            if ((arr[i] - arr[i - 1]) / dist == numberInBetween * dist):
                numberInBetween -= 1
            count += numberInBetween
        return count

# Driver Code
n = 10
arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
k = 9
sol=Solution()
ans=sol.minimiseMaxDistance(arr, k)
print(ans)

