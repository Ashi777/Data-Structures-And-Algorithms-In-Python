class Solution:
    def generateBinaryStrings(self, n):
        self.res = []
        self.backtrack("", n)
        return self.res

    def backtrack(self, curr, n):
            # Base case: if length == n, add to result
            if len(curr) == n:
                self.res.append(curr)
                return
            # Always add '0'
            self.backtrack(curr + '0', n)
            # Add '1' only if previous char not '1'
            if not curr or curr[-1] != '1':
                self.backtrack(curr + '1', n)

