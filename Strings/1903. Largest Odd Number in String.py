class Solution:
    def largestOddNumber(self, num: str) -> str:
        num = num.lstrip("0")  # remove leading zeroes
        for i in range(len(num), 0, -1):
            if int(num[i - 1]) % 2 == 1:  # check if last digit is odd
                return num[:i]
        return ""  # no odd digit found
