class Solution:
    def prefixToPostfix(self, s: str) -> str:
        # Your code goes here
        n = len(s);
        i = n - 1;
        stack = []
        while i >= 0:
            if s[i].isalnum():
                stack.append(s[i])
            else:
                x = stack.pop()
                y = stack.pop()
                new = x + y + s[i]
                stack.append(new)
            i -= 1
        return stack[0]


'''
sol = Solution()
print(sol.prefixToPostfix("+ab"))   
print(sol.prefixToPostfix("*+ab-cd"))     
print(sol.prefixToPostfix("^a*bc"))   


#TC->O(2N)
#SC->O(N)
'''