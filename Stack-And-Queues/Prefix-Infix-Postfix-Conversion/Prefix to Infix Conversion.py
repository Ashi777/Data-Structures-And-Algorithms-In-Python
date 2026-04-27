class Solution:
    def prefixToInfix(self, s: str) -> str:
        # Your code goes here
        n=len(s); i=n-1; stack=[]
        while i>=0:
            if s[i].isalnum():
                stack.append(s[i])
            else:
                x=stack.pop()
                y=stack.pop()
                new="("+x+s[i]+y+")"
                stack.append(new)
            i-=1
        return stack[0]

'''
sol = Solution()
print(sol.prefixToInfix("+ab"))   
print(sol.prefixToInfix("*+ab-cd"))     
print(sol.prefixToInfix("^a*bc"))   


#TC->O(N)+O(N)
#SC->O(N)
'''