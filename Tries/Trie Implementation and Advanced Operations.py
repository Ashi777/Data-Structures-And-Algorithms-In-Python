class Node:
    def __init__(self):
        self.links=[None]*26
        self.countEndWith=0
        self.countPrefix=0

    def containsKey(self, ch):
        return self.links[ord(ch)-ord('a')] is not None

    def get(self, ch):
        return self.links[ord(ch)-ord('a')]

    def put(self, ch, node):
        self.links[ord(ch)-ord('a')]=node

    def increaseEnd(self):
        self.countEndWith+=1

    def increasePrefix(self):
        self.countPrefix+=1

    def deleteEnd(self):
        self.countEndWith-=1

    def reducePrefix(self):
        self.countPrefix-=1

class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node=self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node=node.get(ch)
            node.increasePrefix()
        node.increaseEnd()

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        node=self.root
        for ch in word:
            if node.containsKey(ch):
                node=node.get(ch)
            else:
                return 0
        return node.countEndWith

    def countWordsStartingWith(self, prefix):
        """
        :type word: str
        :rtype: int
        """
        node=self.root
        for ch in prefix:
            if node.containsKey(ch):
                node=node.get(ch)
            else:
                return 0
        return node.countPrefix

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        node=self.root
        for ch in word:
            if node.containsKey(ch):
                node=node.get(ch)
                node.reducePrefix()
            else:
                return
        node.deleteEnd()

