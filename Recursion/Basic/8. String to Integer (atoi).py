class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        # Step 1: skip spaces
        i = self.skip_spaces(0, s)
        if i == len(s):  # empty string after spaces
            return 0
        # Step 2: handle sign
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        # Step 3: read digits recursively
        num, i = self.read_number(i, 0, s)
        num *= sign
        # Step 4: clamp result
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num

    # Recursive helper to skip spaces
    def skip_spaces(self, i, s):
        if i < len(s) and s[i] == " ":
            return self.skip_spaces(i + 1, s)
        return i

    # Recursive helper to read digits
    def read_number(self, i, value, s):
        if i < len(s) and s[i].isdigit():
            value = value * 10 + int(s[i])
            return self.read_number(i + 1, value, s)
        return value, i

