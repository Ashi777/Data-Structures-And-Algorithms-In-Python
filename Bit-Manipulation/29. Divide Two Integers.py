class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==divisor: return 1
        sign=True; ans=0
        if (dividend>=0 and divisor<0): sign = False
        if (dividend<=0 and divisor>0): sign = False
        n=abs(dividend); d=abs(divisor)
        while(n>=d):
            count=0
            while(n>=(d<<(count+1))):    #d*(2**(count+1))
                count+=1
            ans+=1<<count   #2**count
            n=n-(d*(1<<count))
        if ans>=2**31 and sign==True:
            return 2**31-1
        if ans>=2**31 and sign!=True:
            return -2**31
        return ans if sign else -1*ans


# TC -> O((log(base2)N)**2)
# SC -> O(1)