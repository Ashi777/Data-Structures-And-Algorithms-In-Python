class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n=len(a); m=len(b)
        repeat=-(-m//n)
        if b in a*repeat:
            return repeat
        if b in a*(repeat+1):
            return repeat+1
        return -1

