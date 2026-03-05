from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(start):
            # if we've reached the end, success
            if start == n:
                return True
            if start in memo:
                return memo[start]

            # try every possible end index
            for end in range(start + 1, n + 1):
                if s[start:end] in wordSet and dfs(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return dfs(0)

