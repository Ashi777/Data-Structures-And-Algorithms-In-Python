class Solution:
    def bubbleSort(self, nums):
        n=len(nums)
        for i in range(n-1, -1, -1):
            didSwap=0
            for j in range(0, i):
                if nums[j]>nums[j+1]:
                    nums[j+1], nums[j]=nums[j], nums[j+1]
                    didSwap=1
            if didSwap==0: return nums
        return nums

