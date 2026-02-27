class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        # Your code goes here
        n=len(val)
        items=[]
        for i in range(n):
            items.append([val[i]/wt[i], val[i], wt[i]])
        items.sort(reverse=True, key=lambda x: x[0])
        total_value=0.0
        for ratio, value, weight in items:
            if capacity==0:
                break
            if weight<=capacity:
                total_value+=value
                capacity-=weight
            else:
                total_value+=ratio*capacity
                capacity=0
        return round(total_value, 6)

# Driver Code
val = [60,100,120]
wt = [10,20,30]
capacity = 50
sol=Solution()
ans=sol.fractionalKnapsack(val, wt, capacity)
print(ans)

# TC -> O(nlogn + n)
# SC -> O(1)