# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        odd = head # first node
        even = head.next # second node
        even_head = head.next
        while even and even.next:
            odd.next = even.next 
            even.next = odd.next.next
            # move the current odd, even to the next odd, even
            odd = odd.next
            even = even.next
        odd.next = even_head # connect odd and even
        return head
