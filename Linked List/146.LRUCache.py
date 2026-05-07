class Node:
    def __init__(self, key, value):
        # Initialize node with key-value pair and pointers for doubly linked list
        self.key = key
        self.value = value
        self.prev = self.next = None
        
class LRUCache:
    """
    LRU Cache: Implement a Least Recently Used (LRU) cache that supports O(1) get and put operations.
    
    TRICK USED:
    - Combined Data Structures: Use a Hash Map (dictionary) for O(1) access to nodes and a Doubly Linked List (DLL) to maintain the order of use.
    - Sentinel Nodes: Use 'left' and 'right' dummy nodes to represent the Least Recently Used and Most Recently Used ends respectively,
    - avoiding null checks during insertion/removal.
    
    WHY IT WORKS:
    - The Hash Map stores keys pointing to their respective nodes in the DLL, allowing us to jump to any node in O(1).
    - The DLL allows us to remove and re-insert nodes at the "Most Recently Used" (right) position in O(1) time.
    - When the capacity is exceeded, the node immediately following the 'left' sentinel is the oldest and can be evicted in O(1).
    """

    def __init__(self, capacity: int):
        # Set capacity and initialize the hash map for O(1) lookups
        self.cap = capacity
        self.cache = {}
        
        # Initialize sentinel nodes to simplify edge cases in the doubly linked list
        # Left = Least Recently Used (LRU), Right = Most Recently Used (MRU)
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, key: int):
        # If key exists, move the corresponding node to the MRU (right) position
        if key in self.cache:
            # Update order: remove from current position and re-insert at the right
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # Return the value stored in the node
            return self.cache[key].value
        
        # Return -1 if the key is not present in the cache
        return -1
    
    def put(self, key: int, value: int):
        # If the key already exists, remove the old node before updating
        if key in self.cache:
            self.remove(self.cache[key])
            
        # Create a new node, add it to the map, and insert it at the MRU (right) position
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        # If cache exceeds capacity, evict the least recently used item
        if len(self.cache) > self.cap:
            # The LRU node is the one immediately after the left sentinel
            lru = self.left.next
            self.remove(lru)
            # Remove the key from the dictionary to free capacity
            del self.cache[lru.key]
    
    def remove(self, node):
        # Remove a node from the doubly linked list by updating its neighbors
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        # Insert a node at the MRU position (immediately to the left of the right sentinel)
        prev = self.right.prev
        nxt = self.right
        
        # Update pointers to place node between 'prev' and 'right' sentinel
        nxt.prev = node
        prev.next = node
        node.next = nxt
        node.prev = prev



# COMPLEXITY ANALYSIS:
# T(n) = O(1) - Time Complexity
#   - Both get() and put() operations involve dictionary lookups and pointer updates in a DLL, all of which are O(1).
#
# S(n) = O(capacity) - Space Complexity
#   - We store at most 'capacity' number of nodes in both the Hash Map and the Doubly Linked List.