class Solution:
    def partition(self, s: str):
        self.res = []
        self.path = []
        self.backtrack(0, s)
        return self.res

    def isPalindrome(self, sub):
        return sub == sub[::-1]

    def backtrack(self, start, s):
        if start == len(s):
            self.res.append(self.path[:])  # add a copy of current partition
            return
        for end in range(start, len(s)):
            if self.isPalindrome(s[start:end+1]):  # valid palindrome substring
                self.path.append(s[start:end+1])   # choose
                self.backtrack(end+1, s)              # explore
                self.path.pop()                    # unchoose (backtrack)


