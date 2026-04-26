class Solution:
    def infix_to_prefix(self, s: str) -> str:
        # Your code goes here
        self.prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
        # Reverse + swap parentheses
        s = s[::-1].replace('(', '#').replace(')', '(').replace('#', ')')
        # Convert to postfix then reverse
        return self.to_postfix(s)[::-1]

    def to_postfix(self, expr):
        st, out = [], []
        for ch in expr:
            if ch.isalnum():
                out.append(ch)
            elif ch == '(':
                st.append(ch)
            elif ch == ')':
                while st[-1] != '(':
                    out.append(st.pop())
                st.pop()
            else:  # operator
                while st and st[-1] != '(' and (self.prec[st[-1]] > self.prec[ch] or (self.prec[st[-1]] == self.prec[ch] and ch != '^')):
                    out.append(st.pop())
                st.append(ch)
        while st: out.append(st.pop())
        return ''.join(out)

'''
sol = Solution()
print(sol.infix_to_prefix("(a+b)*c"))   # *+abc
print(sol.infix_to_prefix("a+b*c"))     # +a*bc
print(sol.infix_to_prefix("a+b*c^d"))   # +a*b^cd


#TC->O(N)
#SC->O(N)
'''