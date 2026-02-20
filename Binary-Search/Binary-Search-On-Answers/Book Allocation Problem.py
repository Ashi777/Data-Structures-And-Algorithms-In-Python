class Solution:
    def findPages(self, nums, m):
        low = max(nums);
        high = sum(nums)
        while (low <= high):
            mid = (low + high) // 2
            noofstudents = self.students(nums, mid)
            if (noofstudents > m):
                low = mid + 1
            else:
                high = mid - 1
        return low

    def students(self, nums, pages):
        countstudent = 1;
        pagestudent = 0
        for i in range(len(nums)):
            if (pagestudent + nums[i] <= pages):
                pagestudent += nums[i]
            else:
                countstudent += 1
                pagestudent = nums[i]
        return countstudent

# Driver Code
nums = [12, 34, 67, 90]
m=2
sol=Solution()
ans=sol.findPages(nums, m)
print(ans)

# TC -> O(N) * O(log(base2)(sum-max+1))
# SC -> O(1)