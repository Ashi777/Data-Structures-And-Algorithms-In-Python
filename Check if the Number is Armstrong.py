class Solution:
    def isArmstrong(self, n):
        digits = str(n)
        power = len(digits)
        total = sum(int(digit) ** power for digit in digits)
        return total == n

