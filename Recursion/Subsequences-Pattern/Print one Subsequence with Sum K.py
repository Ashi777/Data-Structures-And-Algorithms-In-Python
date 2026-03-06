class Solution:
    def printOneSubsequenceWithTargetSum(self, nums, k):
        def dfs(index, curr_sum, path):
            # Base case: end of array
            if index == len(nums):
                if curr_sum == k:
                    print(path)  # found one subsequence
                    return True
                return False

            # Include nums[index]
            path.append(nums[index])
            if dfs(index + 1, curr_sum + nums[index], path):
                return True
            path.pop()  # backtrack

            # Exclude nums[index]
            if dfs(index + 1, curr_sum, path):
                return True

            return False
        dfs(0, 0, [])
