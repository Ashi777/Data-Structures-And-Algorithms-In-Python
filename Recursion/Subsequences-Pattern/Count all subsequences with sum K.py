class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        def dfs(index, curr_sum):
            # Base case: end of array
            if index == len(nums):
                return 1 if curr_sum == k else 0

            # Include nums[index]
            include = dfs(index + 1, curr_sum + nums[index])

            # Exclude nums[index]
            exclude = dfs(index + 1, curr_sum)

            return include + exclude
        return dfs(0, 0)