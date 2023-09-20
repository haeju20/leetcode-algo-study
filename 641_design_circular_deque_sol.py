class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.max, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: ListNode, new: ListNode):
        next = node.right
        node.right = new
        new.left, new.right = node, next
        next.left = new

    def _del(self, node: ListNode):
        next = node.right.right
        node.right = next
        next.left = node

    # insert into head
    def insertFront(self, value: int) -> bool:
        if self.len == self.max:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    # insert into tail
    def insertLast(self, value: int) -> bool:
        if self.len == self.max:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    # delete from head
    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    # delete from tail
    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        if self.len != 0:
            return self.head.right.val
        else:
            return -1

    def getRear(self) -> int:
        if self.len != 0:
            return self.tail.left.val
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.max
