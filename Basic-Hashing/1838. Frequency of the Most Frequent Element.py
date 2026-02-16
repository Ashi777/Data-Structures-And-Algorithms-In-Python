class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)  # count frequencies
        nums.sort()

        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]  # prefix sum

        res = 0

        for i in range(len(nums)):
            # binary search left boundary
            lo, hi = 0, i
            while lo < hi:
                mid = (lo + hi) // 2
                total = prefix[i+1] - prefix[mid]   # sum of window [mid..i]
                need = (i - mid + 1) * nums[i] - total
                if need <= k:
                    hi = mid
                else:
                    lo = mid + 1

            res = max(res, i - lo + 1)

        return res

'''
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        total = 0
        res = 0
        for r in range(len(nums)):
            total += nums[r]
            # Check cost to make all nums[l..r] = nums[r]
            while (nums[r] * (r - l + 1)) - total > k:
                total -= nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res
'''