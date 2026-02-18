class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0;
        high = n - 1
        ans = n
        while (low <= high):
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

# Driver Code
nums = [1,3,5,6]
target = 5
sol=Solution()
ans=sol.searchInsert(nums, target)
print(ans)

# TC -> O(log(base2)N)
# SC -> O(1)