import math
class Solution:
    def divisors(self, n):
        '''divisors=[]
        for i in range(1,n+1):
            if (n%i==0):
                divisors.append(i)
        return divisors'''

        divisors=[]
        for i in range(1, int(math.sqrt(n))+1):
            if(n%i==0):
                divisors.append(i)
                if(n/i)!=i:
                    divisors.append(int(n/i))
        return sorted(divisors)

