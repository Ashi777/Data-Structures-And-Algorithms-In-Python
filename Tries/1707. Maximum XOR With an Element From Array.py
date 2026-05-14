class Node:
    def __init__(self):
        self.links=[None, None]

    def containsKey(self, bit):
        return self.links[bit] is not None

    def get(self, bit):
        return self.links[bit]

    def put(self, bit, node):
        self.links[bit]=node

class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self, num):
        node=self.root
        for i in range(31, -1, -1):
            bit=(num>>i)&1
            if not node.containsKey(bit):
                node.put(bit, Node())
            node=node.get(bit)

    def findMax(self, num):
        node=self.root
        maxNum=0
        for i in range(31, -1, -1):
            bit=(num>>i)&1
            if node.containsKey(not bit):
                maxNum=maxNum | (1<<i)
                node=node.get(not bit)
            else:
                node=node.get(bit)
        return maxNum

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[0]*len(queries)
        offlineQueries=[]
        nums.sort()
        index=0
        for query in queries:
            offlineQueries.append((query[1], (query[0], index)))
            index+=1
        offlineQueries.sort()
        i=0
        n=len(nums)
        trie=Trie()
        for end, (start, queryIndex) in offlineQueries:
            while i<n and nums[i]<=end:
                trie.insert(nums[i])
                i+=1
            if i!=0:
                ans[queryIndex]=trie.findMax(start)
            else:
                ans[queryIndex]-=1
        return ans

