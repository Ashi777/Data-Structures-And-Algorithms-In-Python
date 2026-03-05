class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math

        numbers = [str(i) for i in range(1, n+1)]
        k -= 1  # convert to 0-indexed
        result = []

        def helper(nums, k):
            if not nums:
                return
            n = len(nums)
            fact = math.factorial(n-1)
            index = k // fact
            result.append(nums[index])
            # remove chosen number
            helper(nums[:index] + nums[index+1:], k % fact)

        helper(numbers, k)
        return "".join(result)


