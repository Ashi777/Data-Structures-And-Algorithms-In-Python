class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()   # sort to group duplicates together

        def backtrack(index, path):
            res.append(path[:])

            for i in range(index, len(nums)):
                # Skip duplicates
                if i > index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res