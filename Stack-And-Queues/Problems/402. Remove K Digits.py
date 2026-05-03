class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)
        for i in range(n):
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        while k > 0:
            stack.pop()
            k -= 1
        res = "".join(stack).lstrip("0")
        return res if res else "0"


'''
# Example usage
sol = Solution()
print(sol.removeKdigits("1432219", 3))   
print(sol.removeKdigits("10200", 1))
print(sol.removeKdigits("10", 2))

# TC -> O(3N)+O(K)
# TC -> O(N)+O(N)
'''