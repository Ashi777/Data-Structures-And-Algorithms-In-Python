class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0; r=0; maxlen=0; zeroes=0
        while(r<len(nums)):
            if nums[r]==0: zeroes+=1
            if zeroes>k:
                if nums[l]==0: zeroes-=1
                l+=1
            if zeroes<=k:
                length=r-l+1
                maxlen=max(maxlen, length)
            r+=1
        return maxlen

