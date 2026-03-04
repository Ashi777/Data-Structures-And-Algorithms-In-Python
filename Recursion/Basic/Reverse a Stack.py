class Solution:
    def reverseStack(self, stack):
        if not stack:
            return
        top = stack.pop()
        self.reverseStack(stack)
        self.insertAtBottom(stack, top)
        return stack

    def insertAtBottom(self, stack, x):
        if not stack:
            stack.append(x)
            return
        top = stack.pop()
        self.insertAtBottom(stack, x)
        stack.append(top)

s=Solution()
stack = [4, 1, 3, 2]
ans=s.reverseStack(stack)
print(ans)  # Output: [2, 3, 1, 4]

stack2 = [10, 20, -5, 7, 15]
ans2=s.reverseStack(stack2)
print(ans2)  # Output: [15, 7, -5, 20, 10]