class Solution:
    def kthElement(self, arr1, arr2, k):
        n1=len(arr1)
        n2=len(arr2)
        if(n1>n2): return self.kthElement(arr2, arr1, k)
        low=max(0, k-n2); high=min(k, n1)
        n=n1+n2
        left=k
        while(low<=high):
            mid1=(low+high)//2
            mid2=left-mid1
            l1, l2 = float('-inf'), float('-inf')
            r1, r2 = float('inf'), float('inf')
            if(mid1<n1): r1=arr1[mid1]
            if(mid2<n2): r2=arr2[mid2]
            if(mid1-1>=0): l1=arr1[mid1-1]
            if(mid2-1>=0): l2=arr2[mid2-1]
            if(l1<=r2 and l2<=r1):
                return max(l1, l2)
            elif(l1>r2): high=mid1-1
            else: low=mid1+1
        return 0

# Driver Code
a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
sol=Solution()
ans=sol.kthElement(a, b, k)
print(ans)

