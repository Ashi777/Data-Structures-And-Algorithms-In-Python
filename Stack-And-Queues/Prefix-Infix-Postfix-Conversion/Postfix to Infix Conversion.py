class Solution:
    def postfix_to_infix(self, s: str) -> str:
        # Your code goes here
        i=0; stack=[]; n=len(s)
        while i<n:
            if s[i].isalnum():
                stack.append(s[i])
            else:
                x=stack.pop()
                y=stack.pop()
                new="("+y+s[i]+x+")"
                stack.append(new)
            i+=1
        return stack[0]


sol = Solution()
print(sol.postfix_to_infix("ab-de+f*/"))


#TC->O(N)+O(N)
#SC->O(N)