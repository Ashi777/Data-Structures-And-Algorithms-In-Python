class Solution:                                         # TC -> O(N)
    def candy(self, ratings: list[int]) -> int:         # SC -> O(1)
        sum1=1; i=1; n=len(ratings)
        while(i<n):
            if(ratings[i]==ratings[i-1]):
                sum1+=1; i+=1; continue
            peak=1
            while(i<n and ratings[i]>ratings[i-1]):
                peak+=1; sum1+=peak; i+=1
            down=1
            while(i<n and ratings[i]<ratings[i-1]):
                sum1+=down; i+=1; down+=1
            if down>peak:
                sum1+=down-peak
        return sum1

'''
class Solution:                                          # TC -> O(2N)
    def candy(self, ratings: List[int]) -> int:          # SC -> O(N)
        n=len(ratings)
        left=[1]*n
        for i in range(1, n):
            if (ratings[i]>ratings[i-1]):
                left[i]=left[i-1]+1
        curr=1; sum1=left[-1]
        for i in range(n-2, -1, -1):
            if ratings[i]>ratings[i+1]:
                curr+=1
            else:
                curr=1
            sum1+=max(left[i], curr)
        return sum1
'''

# Driver Code
ratings = [1,0,2]
sol=Solution()
ans=sol.candy(ratings)
print(ans)

