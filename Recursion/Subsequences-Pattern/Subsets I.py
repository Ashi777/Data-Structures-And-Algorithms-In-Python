class Solution:
    def subsetSums(self, nums):
        #your code goes here
        res = []
        n = len(nums)

        def dfs(index, curr_sum):
            if index == n:
                res.append(curr_sum)
                return
            # Include nums[index]
            dfs(index + 1, curr_sum + nums[index])
            # Exclude nums[index]
            dfs(index + 1, curr_sum)

        dfs(0, 0)
        return res

