class Solution:
    def countOccurrences(self, arr, x):
        # Your code goes here
        n = len(arr)
        first, last = self.firstAndLastPosition(arr, n, x)
        if first == -1:
            return 0
        return last - first + 1

    def firstOccurrence(self, arr, n, k):
        low = 0
        high = n - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            # maybe an answer
            if arr[mid] == k:
                first = mid
                # look for smaller index on the left
                high = mid - 1
            elif arr[mid] < k:
                low = mid + 1  # look on the right
            else:
                high = mid - 1  # look on the left
        return first

    def lastOccurrence(self, arr, n, k):
        low = 0
        high = n - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            # maybe an answer
            if arr[mid] == k:
                last = mid
                # look for larger index on the right
                low = mid + 1
            elif arr[mid] < k:
                low = mid + 1  # look on the right
            else:
                high = mid - 1  # look on the left
        return last

    def firstAndLastPosition(self, arr, n, k):
        first = self.firstOccurrence(arr, n, k)
        if first == -1:
            return (-1, -1)
        last = self.lastOccurrence(arr, n, k)
        return (first, last)

# Driver Code
arr = [0, 0, 1, 1, 1, 2, 3]
x = 1
sol=Solution()
ans=sol.countOccurrences(arr, x)
print(ans)

