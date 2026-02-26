class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxindex=0
        for i in range(len(nums)):
            if i>maxindex:
                return False
            maxindex=max(maxindex, i+nums[i])
        return True

# Driver Code
nums = [2,3,1,1,4]
sol=Solution()
ans=sol.canJump(nums)
print(ans)

# TC -> O(N)
# SC -> O(1)