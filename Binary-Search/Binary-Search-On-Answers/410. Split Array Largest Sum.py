class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low=max(nums); high=sum(nums)
        while(low<=high):
            mid=(low+high)//2
            subarray=self.func(nums, mid)
            if(subarray>k):
                low=mid+1
            else:
                high=mid-1
        return low

    def func(self, nums, subarray):
        countsubarray=1; sumsubarray=0
        for i in range(len(nums)):
            if(sumsubarray+nums[i]<=subarray):
                sumsubarray+=nums[i]
            else:
                countsubarray+=1
                sumsubarray=nums[i]
        return countsubarray

# Driver Code
nums = [7,2,5,10,8]
k = 2
sol=Solution()
ans=sol.splitArray(nums, k)
print(ans)

# TC -> O(N) * O(log(base2)(sum-max+1))
# SC -> O(1)