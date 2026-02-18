class Solution:
    def upperBound(self, nums, x):
        n=len(nums)
        low=0
        high=n-1
        ans=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

# Driver Code
n= 4
nums = [1,2,2,3]
x = 2
sol=Solution()
ans=sol.upperBound(nums, x)
print(ans)

# TC -> O(log(base2)N)
# SC -> O(1)