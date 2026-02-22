class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]; res=""
        for i in s:
            if not stack and i=="(":
                stack.append(i)
            elif stack and i=="(":
                stack.append(i)
                res+=i
            elif len(stack)>1 and i==")":
                stack.pop()
                res+=i
            else:
                stack.pop()
        return res
