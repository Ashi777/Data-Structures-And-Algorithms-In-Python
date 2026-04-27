class Solution:
    def postToPre(self, s: str) -> str:
        # Your code goes here
        i=0; stack=[]; n=len(s)
        while i<n:
            if s[i].isalnum():
                stack.append(s[i])
            else:
                x=stack.pop()
                y=stack.pop()
                new=s[i]+y+x
                stack.append(new)
            i+=1
        return stack[0]

'''
sol = Solution()
print(sol.postToPre("ab+"))   
print(sol.postToPre("abc*+d-"))     
print(sol.postToPre("xyz*+ab/-"))   


#TC->O(N)
#SC->O(N)
'''