class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode) # default

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        if self.table[idx].value is None:
            self.table[idx] = ListNode(key, value)
            return

        p = self.table[idx]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % self.size
        if self.table[idx].value is None:
            return -1

        p = self.table[idx]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.size
        if self.table[idx].value is None:
            return -1

        p = self.table[idx]
        if p.key == key: # if it is the first node
            if p.next is None:
                self.table[idx] = ListNode()
            else:
                self.table[idx] = p.next
            return

        prev = p
        while p: # remove the node of linked list
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
