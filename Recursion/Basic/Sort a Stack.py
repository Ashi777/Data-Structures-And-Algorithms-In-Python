class Solution:
    def insertSorted(self, stack, x):
        if not stack or stack[-1] >= x:
            stack.append(x)
            return
        top = stack.pop()
        self.insertSorted(stack, x)
        stack.append(top)


    def sortStack(self, stack):
        if not stack:
            return
        top = stack.pop()
        self.sortStack(stack)
        self.insertSorted(stack, top)
        return stack


# Example usage
s=Solution()
stack1 = [4, 1, 3, 2]
s.sortStack(stack1)
print(stack1)  # Output: [4, 3, 2, 1]

stack2 = [1]
s.sortStack(stack2)
print(stack2)  # Output: [1]

stack3 = [10, -5, 7, 20, 0]
s.sortStack(stack3)
print(stack3)  # Output: [20, 10, 7, 0, -5]