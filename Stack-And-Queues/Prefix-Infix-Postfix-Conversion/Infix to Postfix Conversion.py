class Solution:
    def infixToPostfix(self, s: str) -> str:
        # Your code goes here
        prec={'+':1, '-':1, '*':2, '/':2, '^':3}
        right_assoc={'^'}
        output=[]
        stack=[]
        for ch in s:
            if ch.isalnum():
                output.append(ch)
            elif ch=='(':
                stack.append(ch)
            elif ch==')':
                while stack and stack[-1]!='(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while (stack and stack[-1]!='(' and (prec[stack[-1]]>prec[ch] or (prec[stack[-1]]==prec[ch] and ch not in right_assoc))):
                    output.append(stack.pop())
                stack.append(ch)
        while stack:
            output.append(stack.pop())
        return ''.join(output)

'''
sol = Solution()
print(sol.infixToPostfix("a+b*c"))     # Output: abc*+
print(sol.infixToPostfix("(a+b)*c"))   # Output: ab+c*
print(sol.infixToPostfix("a+b*c^d"))   # Output: abcd^*+

#TC->O(N)
#SC->O(N)
'''