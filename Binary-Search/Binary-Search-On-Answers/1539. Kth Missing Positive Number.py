class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        low = 0;
        high = len(arr) - 1
        while (low <= high):
            mid = (low + high) // 2
            missing = arr[mid] - (mid + 1)
            if (missing < k):
                low = mid + 1
            else:
                high = mid - 1
        return high + 1 + k

# Driver Code
arr = [2,3,4,7,11]
k = 5
sol=Solution()
ans=sol.findKthPositive(arr, k)
print(ans)

# TC -> O(N)
# SC -> O(1)