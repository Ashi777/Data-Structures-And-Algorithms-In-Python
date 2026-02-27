class Solution:
    def JobScheduling(self, Jobs):
        # Sort jobs by profit in descending order
        Jobs.sort(key=lambda x: x[2], reverse=True)
        total_profit = 0
        count = 0
        # Find the maximum deadline
        max_deadline = max(job[1] for job in Jobs)
        # Initialize the slot array (-1 means empty)
        slots = [-1] * (max_deadline + 1)
        # Place jobs to maximize profit
        for job in Jobs:
            job_id, deadline, profit = job
            # Try to place the job in the latest available slot before its deadline
            for j in range(deadline, 0, -1):
                if slots[j] == -1:
                    slots[j] = job_id
                    total_profit += profit
                    count += 1
                    break
        return count, total_profit

# Driver Code
Jobs = [ [1, 4, 20] , [2, 1, 10] , [3, 1, 40] , [4, 1, 30] ]
sol=Solution()
ans=sol.JobScheduling(Jobs)
print(ans)

# TC -> O(2NlogN + N*max deadlines)
# SC -> O(max deadline)