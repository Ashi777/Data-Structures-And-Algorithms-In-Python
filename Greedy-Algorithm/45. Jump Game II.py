class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps=0; l=0; r=0
        while r<len(nums)-1:
            farthest=0
            for i in range(l, r+1):
                farthest=max(farthest, i+nums[i])
            l=r+1
            jumps+=1
            r=farthest
        return jumps

# Driver Code
nums = [2,3,1,1,4]
sol=Solution()
ans=sol.jump(nums)
print(ans)

# TC -> O(N)
# SC -> O(1)