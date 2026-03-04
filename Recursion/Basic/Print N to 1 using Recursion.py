class Solution:
    def printNumbers(self, n):
        # Your code goes here
        if (n<1):
            return
        print(n)
        self.printNumbers(n-1)

