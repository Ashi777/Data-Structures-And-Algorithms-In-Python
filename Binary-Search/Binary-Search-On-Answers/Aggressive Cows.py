class Solution:
    def aggressiveCows(self, nums, k):
        nums.sort()
        low = 0;
        high = nums[n - 1] - nums[0]
        while (low <= high):
            mid = (low + high) // 2
            if (self.canweplace(nums, mid, k) == True):
                low = mid + 1
            else:
                high = mid - 1
        return high

    def canweplace(self, nums, dist, k):
        countCows = 1;
        last = nums[0]
        for i in range(1, n):
            if (nums[i] - last >= dist):
                countCows += 1
                last = nums[i]
            if (countCows >= k): return True
        return False

# Driver Code
n = 6
k = 4
nums = [0, 3, 4, 7, 10, 9]
sol=Solution()
ans=sol.aggressiveCows(nums, k)
print(ans)

# TC -> O(NlogN) + [O(log(base2)(max-min) * O(N)]
# SC -> O(1)