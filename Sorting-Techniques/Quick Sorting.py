class Solution:
    def quickSort(self, nums):
        def sorting(nums, low, high):
            if (low < high):
                pivot = partition(nums, low, high)
                sorting(nums, low, pivot - 1)
                sorting(nums, pivot + 1, high)

        def partition(nums, low, high):
            pivot = nums[low]
            i = low
            j = high
            while True:
                while (i <= j and nums[i] <= pivot):
                    i += 1
                while (i <= j and nums[j] > pivot):
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    break
            nums[low], nums[j] = nums[j], nums[low]
            return j

        sorting(nums, 0, len(nums) - 1)
        return nums

