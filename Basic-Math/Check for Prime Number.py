import math
class Solution:
    def isPrime(self, n):
        '''divisors=[]
        #your code goes here
        for i in range(1,n+1):
            if n%i==0:
                divisors.append(i)
        return (len(divisors)==2)'''
        divisors=[]
        #your code goes here
        for i in range(1,int(math.sqrt(n))+1):
            if (n%i==0):
                divisors.append(i)
                if (n/i)!=i:
                    divisors.append(int(n/i))
        return (len(divisors)==2)

