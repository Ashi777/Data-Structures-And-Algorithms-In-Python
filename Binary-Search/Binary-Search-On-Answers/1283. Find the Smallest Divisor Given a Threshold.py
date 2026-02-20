import math


class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        n = len(nums)
        # if(n<threshold): return -1
        low = 1;
        high = max(nums);
        ans = -1
        while (low <= high):
            mid = (low + high) // 2
            if (self.sumofD(nums, mid) <= threshold):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def sumofD(self, nums, div):
        sum1 = 0;
        n = len(nums)
        for i in range(n):
            sum1 += math.ceil(nums[i] / div)
        return sum1

# Driver Code
nums = [1,2,5,9]
threshold = 6
sol=Solution()
ans=sol.smallestDivisor(nums, threshold)
print(ans)

