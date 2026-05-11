class Solution:
    def celebrity(self, M):
        n=len(M); top=0; down=n-1
        while top<down:
            if M[top][down]==1:
                top=top+1
            else:
                down-=1
        for i in range(n):
            if i==top:
                continue
            if M[top][i]==1 or M[i][top]==0:
                return -1
        return top


sol = Solution()
print(sol.celebrity([ [0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0] ]))
print(sol.celebrity([ [0, 1], [1, 0] ]))
print(sol.celebrity([ [0, 1, 0], [0, 0, 0], [0, 1, 0] ]))


# TC -> O(2N)
# TC -> O(1)