class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = self.next = None
        
class LRUCace:
    
    def __init__(self,capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self,key:int):
        if key in self.cache:
            #need to reomve the node, insert it to the right and return self.cachce[key]
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cachce[key].value
        #else return -1 beacause the key doesnt exists
        return -1
    
    def put(self,key:int,value:int):
        if key in self.cache:
            #if the key exists, we remove it
            self.remove(self.cache[key])
        #now we create a new node with key and value
        #and we need to insert the node 
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            #if there are too many items in our cache, we need to remove the LRU
            #need to find the lru(it is the leftmost node)
            lru = self.left.next
            self.remove(lru)
            #now we need to delete it from the cache
            del self.cache[lru.key]
    
    def remove(self,node):
        #we are getting a node and need to remove it from the dlinklist
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self,node):
        #we need to take the node we got and insert it to the right of the dlinkedlist
        prev = self.right.prev
        nxt = self.right
        nxt.prev = node
        prev.next = node
        node.next = nxt
        node.prev = prev