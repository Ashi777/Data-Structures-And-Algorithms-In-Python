class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n):
            # Assume the minimum is the current element
            min_index = i
            # Find the smallest element in the unsorted part
            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            # Swap the found minimum element with the first element of the unsorted part
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

