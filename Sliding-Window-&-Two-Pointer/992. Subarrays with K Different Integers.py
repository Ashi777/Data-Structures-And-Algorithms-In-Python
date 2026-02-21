from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k)-self.atMost(nums, k-1)

    def atMost(self, nums, k):
        l=0; r=0; count=0; mpp=defaultdict(int)
        while(r<len(nums)):
            mpp[nums[r]]+=1
            while(len(mpp)>k):
                mpp[nums[l]]-=1
                if(mpp[nums[l]]==0):
                    del mpp[nums[l]]
                l+=1
            count+=r-l+1
            r+=1
        return count

