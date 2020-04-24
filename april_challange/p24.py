class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lru_tail = None
        self.lru_head = None
        self.items = {}

    def evict(self):
        tmp_tail = self.lru_tail.next
        del self.items[self.lru_tail.val]
        if tmp_tail:
            tmp_tail.prev = None
        self.lru_tail = tmp_tail

    def join(self, n1, n2):
        if n1:
            n1.next = n2
        if n2:
            n2.prev = n1

    def get(self, key: int) -> int:
        val, node = self.items.get(key, [-1, None])
        if val == -1:
            return -1

        if node.next is None:
            return val
        
        if node.prev is None:
            if node.next is not None:
                self.lru_tail = node.next
            else:
                return val

        self.join(node.prev, node.next)

        self.lru_head.next = node
        node.prev = self.lru_head
        self.lru_head = node
        self.lru_head.next = None
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.items[key][0] = value
            self.get(key)
            return
        if len(self.items) == self.cap:
            self.evict()
        node = Node(key)
        if self.lru_head:
            self.lru_head.next = node
            node.prev = self.lru_head
        self.lru_head = node
        if not self.lru_tail:
            self.lru_tail = self.lru_head
        self.items[key] = [value, node]
        


def print_ll(node):
    while node:
        print(node.val)
        node = node.next
    print('--------')

# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)
cache.put(2,1)
cache.put(2,2)
print(cache.get(2))
# cache.put(3,2)
# print(cache.get(2))
# print(cache.get(3))