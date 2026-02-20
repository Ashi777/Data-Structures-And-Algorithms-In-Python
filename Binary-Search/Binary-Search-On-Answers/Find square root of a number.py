class Solution:
    def floorSqrt(self, n: int) -> int:
        low=1
        high=n
        while low<high:
            mid=(low+high)//2
            if mid*mid==n:
                return mid
            if mid*mid>n:
                high=mid-1
            else:
                low=mid+1
        return mid

# Driver Code
n = 36
sol=Solution()
ans=sol.floorSqrt(n)
print(ans)

# TC -> O(log(base2)N)
# SC -> O(1)