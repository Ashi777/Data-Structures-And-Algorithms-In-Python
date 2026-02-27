class Solution:
    def findPlatform(self, Arrival, Departure):
        #your code goes here
        Arrival.sort(); Departure.sort(); n=len(Arrival)
        i=0; j=0; count=0; maxCount=0
        while(i<n):
            if(Arrival[i]<=Departure[j]):
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            maxCount=max(maxCount, count)
        return maxCount

# Driver Code
Arrival = [900, 940, 950, 1100, 1500, 1800]
Departure = [910, 1200, 1120, 1130, 1900, 2000]
sol=Solution()
ans=sol.findPlatform(Arrival, Departure)
print(ans)

# TC -> O(2NlogN + N)
# SC -> O(1)