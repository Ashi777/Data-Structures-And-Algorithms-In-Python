class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start != 0 or goal != 0:
            count += (start & 1) ^ (goal & 1)
            start = start >> 1
            goal = goal >> 1
        return count


'''class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_val = start ^ goal
        return bin(xor_val).count("1")    #bin() for binary
'''