class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1              # 🔹 NEW: track frequency
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert_front(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        self.size -= 1

    def remove_last(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0                           # 🔹 NEW: track min frequency
        self.node_map = {}                          # key -> Node
        self.freq_map = {}                          # freq -> DoublyLinkedList

    def _update(self, node):
        """ 🔹 NEW: move node to higher freq list """
        freq = node.freq
        self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]
            if self.min_freq == freq:               # update min_freq if needed
                self.min_freq += 1
        node.freq += 1
        self.freq_map.setdefault(node.freq, DoublyLinkedList()).insert_front(node)

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._update(node)                          # 🔹 increase frequency
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self._update(node)
            return

        if len(self.node_map) >= self.capacity:
            # 🔹 Evict LFU node (use min_freq)
            lfu_list = self.freq_map[self.min_freq]
            lfu_node = lfu_list.remove_last()
            del self.node_map[lfu_node.key]

        # insert new node
        node = Node(key, value)
        self.node_map[key] = node
        self.freq_map.setdefault(1, DoublyLinkedList()).insert_front(node)
        self.min_freq = 1                           # 🔹 reset min_freq

