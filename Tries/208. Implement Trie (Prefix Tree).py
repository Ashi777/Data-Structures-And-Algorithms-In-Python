class Node:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def setEnd(self):
        self.flag = True

    def isEnd(self):
        return self.flag


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
        node.setEnd()

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return node.isEnd()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return True

