class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        def recursion(base, power):
            if power == 0:
                return 1
            if power % 2 == 0:
                return recursion((base ** 2) % mod, power // 2)
            else:
                return base * recursion((base ** 2) % mod, power // 2)
        return (recursion(5, (n + 1) // 2) * recursion(4, (n // 2))) % mod


'''
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_pos = (n + 1) // 2
        odd_pos = n // 2
        return (pow(5, even_pos, MOD) * pow(4, odd_pos, MOD)) % MOD
'''