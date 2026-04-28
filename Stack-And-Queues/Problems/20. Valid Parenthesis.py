class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in "([{":  # If opening bracket, push to stack
                stack.append(ch)
            else:  # Closing bracket
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
        return not stack

