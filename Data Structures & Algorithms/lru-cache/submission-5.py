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
    def addToEnd(self, node):
        tmp = self.tail.prev
        self.tail.prev = node
        tmp.next = node
        node.prev = tmp
        node.next = self.tail
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.addToEnd(node)
        return node.val
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]
            self.cache[key] = ListNode(key,value)
            self.addToEnd(self.cache[key])
            return
        self.remove(self.cache[key])
        self.cache[key] = ListNode(key,value)
        self.addToEnd(self.cache[key])




            
        
