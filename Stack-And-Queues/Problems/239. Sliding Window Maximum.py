from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        dq=deque()
        res=[]
        for i, val in enumerate(nums):
            if dq and dq[0]<=i-k:
                dq.popleft()
            while dq and nums[dq[-1]]<val:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                res.append(nums[dq[0]])
        return res


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
print(sol.maxSlidingWindow([1], 1))                  # [1]


# TC -> O(2N)
# TC -> O(K)+O(N-K)