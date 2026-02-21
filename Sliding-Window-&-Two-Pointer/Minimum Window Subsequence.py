class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)
        min_len = float("inf")
        start = -1

        i = 0
        while i < n:
            j = 0
            # Match subsequence
            while i < n:
                if s1[i] == s2[j]:
                    j += 1
                    if j == m:  # found full subsequence
                        break
                i += 1

            if j < m:  # subsequence not found
                break

            # Backtrack to minimize window
            end = i
            j -= 1
            while j >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                i -= 1
            i += 1  # move to window start
            if end - i + 1 < min_len:
                min_len = end - i + 1
                start = i

            # Move to next possible window
            i = i + 1

        return "" if start == -1 else s1[start:start + min_len]