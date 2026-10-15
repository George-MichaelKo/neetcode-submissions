class Node:
    def __init__(self):
        self.key = None
        self.val = None
        self.prev = None
        self.next = None
class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        nxt_node = self.head.next
        self.head.next = node
        node.next = nxt_node
        node.prev = self.head
        nxt_node.prev = node

    def delete_last(self):
        node = self.tail.prev
        prev = node.prev
        self.tail.prev = prev
        prev.next = self.tail
        return node

    def delete_mid(self, node):
        previous = node.prev
        nxt_node = node.next
        previous.next = nxt_node
        nxt_node.prev = previous

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = dict() # key: key node    
        self.cache = DoubleLinkedList()

    def get(self, key: int) -> int:
        if not key in self.hashMap:
            return -1
        node = self.hashMap[key]
        self.cache.delete_mid(node)
        self.cache.add(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key not in self.hashMap:
            
            new_node = Node()
            new_node.key = key
            new_node.val = value
            self.hashMap[key] = new_node
            self.cache.add(new_node)
            if len(self.hashMap) > self.capacity:
                last_node = self.cache.delete_last()
                del self.hashMap[last_node.key]
        else:
            self.hashMap[key].val = value
            new_node = self.hashMap[key]
            self.cache.delete_mid(new_node)
            self.cache.add(new_node)

            

        
