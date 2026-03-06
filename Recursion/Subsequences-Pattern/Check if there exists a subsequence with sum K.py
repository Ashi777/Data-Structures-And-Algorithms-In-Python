class Solution:
    def checkSubsequenceSum(self, nums, k):
        def dfs(index, curr_sum):
            # Base case: sum found
            if curr_sum == k:
                return True
            # Out of bounds
            if index == len(nums):
                return False

            # Include current element
            if dfs(index + 1, curr_sum + nums[index]):
                return True

            # Exclude current element
            if dfs(index + 1, curr_sum):
                return True

            return False

        return dfs(0, 0)
