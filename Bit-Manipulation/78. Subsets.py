class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for num in range(1 << n):   # from 0 to 2^n - 1
            subset = []
            for i in range(n):
                if num & (1 << i):  # check if i-th bit is set
                    subset.append(nums[i])
            res.append(subset)
        return res
