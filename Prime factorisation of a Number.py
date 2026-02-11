class Solution:
    def primeFactors(self, queries):
        #your code goes here
        result = []
        for q in queries:
            result.append(self.factorize(q))
        return result


    def factorize(self, num):
        factors = []
        # Check for factor 2
        while num % 2 == 0:
            factors.append(2)
            num //= 2
        # Check for odd factors
        p = 3
        while p * p <= num:
            while num % p == 0:
                factors.append(p)
                num //= p
            p += 2
        # If num is prime and > 2
        if num > 1:
            factors.append(num)
        return factors
