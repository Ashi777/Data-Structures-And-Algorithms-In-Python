class Solution:
    def trap(self, height):
        lmax=rmax=total=0; n=len(height)
        l=0; r=n-1
        while l<r:
            if height[l]<=height[r]:
                if lmax>height[l]:
                    total+=lmax-height[l]
                else:
                    lmax=height[l]
                l+=1
            else:
                if rmax>height[r]:
                    total+=rmax-height[r]
                else:
                    rmax=height[r]
                r-=1
        return total


# Example usage
sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trap([4,2,0,3,2,5]))

# TC -> O(N)
# TC -> O(1)