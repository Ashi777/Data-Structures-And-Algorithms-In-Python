class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMost(nums, goal)-self.atMost(nums, goal-1)

    def atMost(self, nums, goal):
        if goal<0: return 0
        l=0; r=0; sum1=0; count=0
        while(r<len(nums)):
            sum1+=nums[r]
            while(sum1>goal):
                sum1-=nums[l]
                l+=1
            count+=r-l+1
            r=r+1
        return count

