class Solution:
    def countPalindromes(self, s: str) -> int:
        """
        For each character, can check it's the first char in how many sequences

        # Find how many pairs
        """
        MOD = 10 ** 9 + 7
        digits = [str(i) for i in range(10)]

        # look for X Y _ Y X

        out = 0
        for x in digits:
            for y in digits:
                out = (out + self.count(x, y, s)) % MOD

        return out

    def count(self, x, y, s):
        # vars defining counts seen so far
        ones = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0

        for char in s:
            old_ones = ones
            old_twos = twos
            if char == x:
                ones += 1
                fives += fours
            if char == y:
                twos += old_ones
                fours += threes
            threes += old_twos
        return fives