# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        node = start = ListNode(None)
        node.next = head
        # start node is prev node of left node
        for _ in range(left - 1):
            start = start.next
        r_node = start.next

        for _ in range(right - left):
            l_node = start.next # l_node is already fixed
            start.next = r_node.next
            r_node.next = r_node.next.next # only r_node moves to the right
            start.next.next = l_node
        return node.next
