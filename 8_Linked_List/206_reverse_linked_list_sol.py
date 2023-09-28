class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, rev = head, None
        while node:
            # node_next is the next pointer of curr node
            # node.next is the prev pointer of curr node
            node_next, node.next = node.next, rev
            # move the curr node to next node
            rev, node = node, node_next
        return rev
