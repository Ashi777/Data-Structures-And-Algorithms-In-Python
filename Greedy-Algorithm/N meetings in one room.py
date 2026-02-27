class Solution:
    def maxMeetings(self, start, end):
        #your code goes here
        arr=[]
        # Create a list of tuples: (start, end, position)
        for i in range(len(start)):
            arr.append((start[i], end[i], i + 1))
        arr.sort(key=lambda x: x[1])
        count=1; freetime=arr[0][1]; ds=[arr[0][2]]
        for i in range(1, len(start)):
            if arr[i][0]>freetime:
                count+=1
                freetime=arr[i][1]
                ds.append(arr[i][2])
        return count

# Driver Code
Start = [1, 3, 0, 5, 8, 5]
End = [2, 4, 6, 7, 9, 9]
sol=Solution()
ans=sol.maxMeetings(Start, End)
print(ans)

# TC -> O(2N + NlogN)
# SC -> O(3N) + O(N)