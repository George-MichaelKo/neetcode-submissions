#ddlinkedlist 
# keyy, value, next prev
class Node:
    def __init__(self):
        self.key = None
        self.val = None
        self.next = None
        self.prev = None
    
class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        nxt_node = self.head.next
        node.next = nxt_node
        node.prev = self.head
        nxt_node.prev = node
        self.head.next = node
    
    def delete_last(self):
        last_node = self.tail.prev
        prev = last_node.prev
        self.tail.prev = prev
        prev.next = self.tail
        return last_node.key

    def delete_mid(self, node):
        prev = node.prev
        nxt_node = node.next
        prev.next = nxt_node
        nxt_node.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        #cpaity
        # hashMap key: node Key
        #DoubleLinked List
        self.capacity = capacity
        self.lru = DoubleLinkedList()
        self.hashMap = dict()
        
    def get(self, key: int) -> int:
        # if in cache return 
        
        if key not in self.hashMap:
            return -1
        node = self.hashMap[key]
        self.lru.delete_mid(node)
        self.lru.add(node)
        return self.hashMap[key].val
        #else return -1
        
    def put(self, key: int, value: int) -> None:
        # check if within capcity else delete last 
             #crete node and add and key : value
        if key in self.hashMap:
            node = self.hashMap[key]
            node.val = value
            self.lru.delete_mid(node)
            self.lru.add(node)
            return
            
        if len(self.hashMap) >= self.capacity:
            node_key = self.lru.delete_last()
            self.hashMap.pop(node_key)
        node = Node()
        node.val = value
        node.key = key
        self.hashMap[key] = node
        self.lru.add(node)


        
