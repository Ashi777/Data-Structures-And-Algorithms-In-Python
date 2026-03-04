class Solution:
  def printNumbers(self, n, num=1):
    if num > n:
      return
    print(num)
    self.printNumbers(n, num + 1)

