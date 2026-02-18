class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first=self.findFirst(nums, target)
        if first==-1: return [-1, -1]
        last=self.findLast(nums, target)
        return [first, last]

    def findFirst(self, nums, target):
        n=len(nums)
        low=0; high=n-1
        first=-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                first=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return first

    def findLast(self, nums, target):
        n=len(nums)
        low=0; high=n-1
        last=-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                last=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return last

# Driver Code
nums = [5,7,7,8,8,10]
target = 8
sol=Solution()
ans=sol.searchRange(nums, target)
print(ans)

# TC -> O(log(base2)N)
# SC -> O(1)