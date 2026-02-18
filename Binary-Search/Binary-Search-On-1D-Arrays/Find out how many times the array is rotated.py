class Solution:
    def findKRotation(self, nums):
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return mid

# Driver Code
nums = [4, 5, 6, 7, 0, 1, 2, 3]
sol=Solution()
ans=sol.findKRotation(nums)
print(ans)

# TC -> O(log(base2)N)
# SC -> O(1)