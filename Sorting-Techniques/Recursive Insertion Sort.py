class Solution:
    def insertionSort(self, nums):
        def sort(n):
            if n <= 1: return
            sort(n - 1)
            last = nums[n - 1]
            j = n - 2

            def insert(j):
                if j >= 0 and nums[j] > last:
                    nums[j + 1] = nums[j]
                    insert(j - 1)
                else:
                    nums[j + 1] = last

            insert(j)

        sort(len(nums))
        return nums

