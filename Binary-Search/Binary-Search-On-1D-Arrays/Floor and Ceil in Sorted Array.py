class Solution:
    def getFloorAndCeil(self, nums, x):
        n = len(nums)
        low = 0
        high = n - 1
        floor = -1
        ceil = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == x:
                return x, x  # Both floor and ceil are x
            elif nums[mid] < x:
                floor = nums[mid]  # Candidate for floor
                low = mid + 1
            else:
                ceil = nums[mid]  # Candidate for ceil
                high = mid - 1

        return floor, ceil

# Driver Code
nums = [2,5,6,0,0,1,2]
target = 0
sol=Solution()
ans=sol.getFloorAndCeil(nums, x)
print(ans)

# TC -> O(log(base2)N)
# SC -> O(1)