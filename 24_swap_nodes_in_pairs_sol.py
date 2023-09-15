# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # swap values only
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            # swap the values
            node.val, node.next.val = node.next.val, node.val
            # move the current node to the next
            node = node.next.next
        return head

# class Solution2: # iterate the swap
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         root = prev = ListNode(None)
#         prev.next = head
#
#         while head and head.next:
#             # swap head and head.next
#             # assign head to head.next.next
#             b = head.next
#             head.next = b.next
#             b.next = head
#             # assign prev to b
#             prev.next = b
#             # move the current node to the next
#             head = head.next
#             prev = prev.next.next
#
#         return root.next

# class Solution3: # recursive the swap
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head and head.next:
#             node = head.next
#             head.next = self.swapPairs(node.next)
#             node.next = head
#             return node
#         return head
