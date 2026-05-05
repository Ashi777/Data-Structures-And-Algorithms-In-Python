class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.index=-1

    def next(self, price: int) -> int:
        self.index+=1
        while self.stack and self.stack[-1][0]<=price:
            self.stack.pop()
        if not self.stack:
            ans = self.index + 1
        else:
            ans = self.index - self.stack[-1][1]
        self.stack.append([price, self.index])
        return ans


stockSpanner = StockSpanner()
print(stockSpanner.next(100)) # 1
print(stockSpanner.next(80))  # 1
print(stockSpanner.next(60))  # 1
print(stockSpanner.next(70))  # 2
print(stockSpanner.next(60))  # 1
print(stockSpanner.next(75))  # 4
print(stockSpanner.next(85))  # 6

# TC -> O(2N)
# TC -> O(N)
