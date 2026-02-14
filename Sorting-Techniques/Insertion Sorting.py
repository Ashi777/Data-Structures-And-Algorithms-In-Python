class Solution:
    def insertionSort(self, nums):
        n=len(nums)
        for i in range(0, n):
            j=i
            while(j>0 and nums[j-1]>nums[j]):
                nums[j-1], nums[j]=nums[j], nums[j-1]
                j-=1
        return nums

