class MinStack:
    def __init__(self):
        self.mini=10**9
        self.stack=[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.mini=val
            self.stack.append(val)
        else:
            if val<self.mini:
                self.stack.append(2*val - self.mini)
                self.mini=val
            else:
                self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return None
        val=self.stack.pop()
        if val<self.mini:
            self.mini=2*self.mini-val

    def top(self) -> int:
        val=self.stack[-1]
        if val<self.mini:
            return self.mini
        return val

    def getMin(self) -> int:
        return self.mini

