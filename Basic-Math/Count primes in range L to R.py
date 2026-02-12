class Solution:
    def primesInRange(self, queries):
        #your code goes here
        arr=[]
        prime=self.getSieve(10**6)
        count=0
        for i in range(2, 10**6):
            count+=prime[i]
            prime[i]=count
        for i in range(0, len(queries)):
            l=queries[i][0]
            r=queries[i][1]
            arr.append(prime[r]-prime[l-1])
        return arr

    def getSieve(self, n: int) -> int:
        if n < 2:
            return 0
        arr=[]
        sieve = [True] * n
        sieve[0] = sieve[1] = False
        i = 2
        while i * i < n:
            if sieve[i]:
                for j in range(i * i, n, i):
                    sieve[j] = False
            i += 1
        return sieve


