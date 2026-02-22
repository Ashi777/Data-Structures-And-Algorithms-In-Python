class Solution:
    def countRev(self, s: str) -> int:
        n=len(s); open_count=0; close_count=0
        if n%2==1: return -1
        for i in s:
            if i=="(":
                open_count+=1
            else:
                if open_count>0:
                    open_count-=1
                else:
                    close_count+=1
        return (open_count+1)//2 + (close_count+1)//2

