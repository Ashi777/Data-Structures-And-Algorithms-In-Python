class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k)-self.atMost(nums, k-1)

    def atMost(self, nums, k):
        if k<0: return 0
        l=0; r=0; sum1=0; count=0
        while(r<len(nums)):
            sum1+=(nums[r]%2)
            while(sum1>k):
                sum1-=(nums[l]%2)
                l+=1
            count+=r-l+1
            r+=1
        return count
