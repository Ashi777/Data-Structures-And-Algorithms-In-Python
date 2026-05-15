class Node:
    def __init__(self):
        self.links=[None]*26
        self.flag=False

    def containsKey(self, ch):
        return self.links[ord(ch)-ord('a')] is not None

    def put(self, ch, node):
        self.links[ord(ch)-ord('a')]=node

    def get(self, ch):
        return self.links[ord(ch)-ord('a')]

    def setEnd(self):
        self.flag=True

    def isEnd(self):
        return self.flag

class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self, word):
        node=self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node=node.get(ch)
        node.setEnd()

    def checkIfPrefixExist(self, word):
        node=self.root
        for ch in word:
            if not node.containsKey(ch):
                return False
            node=node.get(ch)
            if not node.isEnd():
                return False
        return True

class Solution:
    def completeString(self, nums):
        #your code goes here
        trie=Trie()
        for word in nums:
            trie.insert(word)
        longest=""
        for word in nums:
            if trie.checkIfPrefixExist(word):
                if len(word)>len(longest) or (len(word)==len(longest) and word<longest):
                    longest=word
        return longest if longest else "None"

