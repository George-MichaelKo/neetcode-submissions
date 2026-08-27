class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node): #insert at rightmost
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node


    def remove(self, node): #remove at leftmost most which is most recent
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            old_node.value = value
            self.remove(old_node)
            self.insert(old_node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert(new_node)

        if len(self.cache) > self.capacity:
            stale_node = self.left.next
            self.remove(stale_node)
            del self.cache[stale_node.key]
     
 
        
