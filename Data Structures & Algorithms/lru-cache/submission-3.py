class ListNode:
    def __init__(self, key: int = 0, val: int = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def add_to_end(self, node):
        old_prev = self.tail.prev
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        old_prev.next = node
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add_to_end(node)
        return node.val
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add_to_end(node)
        else:
            if len(self.cache) >= self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]
            node = ListNode(key,value)
            self.cache[key] = node
            self.add_to_end(node)




            
        
