class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0;
        high = n - 1
        while (low <= high):
            mid = (low + high) // 2
            if nums[mid] == target: return mid
            # right sorted
            if (nums[low] <= nums[mid]):
                if (nums[low] <= target and target <= nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            # left sorted
            else:
                if (nums[mid] <= target and target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

# Driver Code
nums = [4,5,6,7,0,1,2]
target = 0
sol=Solution()
ans=sol.search(nums, target)
print(ans)

