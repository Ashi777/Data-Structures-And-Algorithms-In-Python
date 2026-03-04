class Solution:
    def helper(self,n):
        if n<=1:
            return n
        return self.helper(n-1)+self.helper(n-2)
    def fib(self, n: int) -> int:
        return self.helper(n)


'''class Solution:
    def fib(self, n: int) -> int:
        if(n<=1): return n
        last=self.fib(n-1)
        slast=self.fib(n-2)
        return last+slast
'''