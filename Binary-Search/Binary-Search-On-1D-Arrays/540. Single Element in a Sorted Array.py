class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if (n==1): return nums[0]
        if (nums[0]!=nums[1]): return nums[0]
        if (nums[n-1]!=nums[n-2]): return nums[n-1]
        low=1; high=n-2
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            #left side
            if (mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1]):
                low=mid+1
            #right side
            else:
                high=mid-1
        return -1

# Driver Code
nums = [1,1,2,3,3,4,4,8,8]
sol=Solution()
ans=sol.singleNonDuplicate(nums)
print(ans)

# TC -> O(log(base2)N)
# SC -> O(1)