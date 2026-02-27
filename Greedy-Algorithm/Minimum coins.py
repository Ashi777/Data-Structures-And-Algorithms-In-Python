class Solution:
    def MinimumCoins(self, coins, amount):
        ans = [];
        count = 0;
        n = len(coins)
        for i in range(n - 1, -1, -1):
            while amount >= coins[i]:
                amount -= coins[i]
                ans.append(coins[i])
                count += 1
        return count if amount == 0 else -1

# Driver Code
coins = [1, 2, 5]
amount = 11
sol=Solution()
ans=sol.MinimumCoins(coins, amount)
print(ans)

# TC -> O(amount)
# SC -> O(1)