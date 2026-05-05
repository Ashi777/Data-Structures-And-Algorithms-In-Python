from typing import List

class Solution:
    def nextGreaterElements(self, nums):
        stack = []; n=len(nums)
        next_greater = [-1]*n
        # Traverse nums2 from right to left
        for i in range(2*n-1, -1, -1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if i<n:
                next_greater[i] = stack[-1] if stack else -1
            stack.append(nums[i%n])

        # Build result for nums1
        return next_greater

'''
# Example usage
sol = Solution()
print(sol.nextGreaterElements([1,2,1]))  # [-1, 3, -1]
print(sol.nextGreaterElements([1,2,3,4,3]))    # [3, -1]

#TC->O(4N)
#SC->O(2N)
'''