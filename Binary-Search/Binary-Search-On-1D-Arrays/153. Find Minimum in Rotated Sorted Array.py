class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0;
        high = n - 1
        ans = float('inf')
        while (low <= high):
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                high = mid - 1
        return ans

# Driver Code
nums = [3,4,5,1,2]
sol=Solution()
ans=sol.findMin(nums)
print(ans)

# TC -> O(log(base2)N)
# SC -> O(1)