class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]; n=len(asteroids)
        for i in range(n):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            else:
                while stack and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
                    stack.pop()
                if stack and stack[-1]==abs(asteroids[i]):
                    stack.pop()
                elif not stack or stack[-1]<0:
                    stack.append(asteroids[i])
        return stack

'''
# Example usage
sol = Solution()
print(sol.asteroidCollision([5,10,-5]))   
print(sol.asteroidCollision([8,-8]))
print(sol.asteroidCollision([10,2,-5]))   

# TC -> O(2N)
# TC -> O(N)
'''
