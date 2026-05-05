from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        # Traverse nums2 from right to left
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            next_greater[num] = stack[-1] if stack else -1
            stack.append(num)

        # Build result for nums1
        return [next_greater[num] for num in nums1]


# Example usage
sol = Solution()
print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))  # [-1, 3, -1]
print(sol.nextGreaterElement([2,4], [1,2,3,4]))    # [3, -1]

#TC->O(2N)
#SC->O(N)+O(N)