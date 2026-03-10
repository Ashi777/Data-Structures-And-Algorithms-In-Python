class Solution:
    def unique_binary_tree(self, a, b):
        #your code goes here
        if (a == 2 and b in [1, 3]) or (b == 2 and a in [1, 3]):
            return True
        return False

