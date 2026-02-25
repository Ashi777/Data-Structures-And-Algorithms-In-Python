class Solution:
    def findRangeXOR(self, l, r):
        #your code goes here
        return self.xor_upto(l-1) ^ self.xor_upto(r)

    def xor_upto(self, n):
            if n % 4 == 0: return n
            if n % 4 == 1: return 1
            if n % 4 == 2: return n + 1
            return 0

# TC -> O(1)
# SC -> O(1)