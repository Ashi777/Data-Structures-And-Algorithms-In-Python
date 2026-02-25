class Solution:
    def checkIthBit(self, n: int, i: int) -> bool:
        # Your code goes here
        return (n & (1 << i)) != 0

# TC -> O(1)
# SC -> O(1)