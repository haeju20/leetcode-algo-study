# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = '', ''
        sum = 0
        head = None
        # linked list -> string
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        sum = int(s1[::-1]) + int(s2[::-1])
        # string of sum -> linked list of sum
        for i in str(sum):
            node = ListNode(int(i))
            node.next, head = head, node
        return node

# class Solution2: # using Full Adder
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         root = head = ListNode(0)
#         carry = 0
#         while l1 or l2 or carry:
#             sum = 0 # sum of digit
#             if l1:
#                 sum += l1.val
#                 l1 = l1.next
#             if l2:
#                 sum += l2.val
#                 l2 = l2.next
#             carry, val = divmod(sum + carry, 10)
#             head.next = ListNode(val)
#             head = head.next
#         return root.next
