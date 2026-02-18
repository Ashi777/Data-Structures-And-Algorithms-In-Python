class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        low=0; high=n-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return -1

# Driver Code
nums = [-1,0,3,5,9,12]
target = 9
sol=Solution()
ans=sol.search(nums, target)
print(ans)

# TC -> O(log(base2)N)
# SC -> O(1)