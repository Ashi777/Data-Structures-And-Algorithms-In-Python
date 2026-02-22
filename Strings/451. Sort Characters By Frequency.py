from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        # Count frequencies of each character
        freq = Counter(s)
        # Sort characters by frequency (descending)
        sorted_chars = sorted(freq.keys(), key=lambda c: freq[c], reverse=True)
        # Build result string
        res = []
        for ch in sorted_chars:
            res.append(ch * freq[ch])
        return "".join(res)