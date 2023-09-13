# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head != None: # to list
            arr.append(head.val)
            head = head.next
        if arr == arr[::-1]: # if palindrome
            return True
        else:
            return False
        # if arr.pop(0) != arr.pop(): return False

# class Solution2: # using Deque
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         d = collections.deque()
#         while head != None: # to deque
#             d.append(head.val)
#             head = head.next
#         while len(d) > 1:
#             if d.popleft() != d.pop(): # optimize
#                 return False
#         return True


# class Solution3: # using Runner (solve the problem as Linked List)
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         rev = None
#         slow = fast = head
#         # make reverse Linked List
#         while fast and fast.next: # fast runs 2 times faster than slow
#             fast = fast.next.next
#             rev, rev.next, slow = slow, rev, slow.next # append the value to the front
#         if fast: # in the case of odd, center value exists
#             slow = slow.next # center value is not included in checking palindrome
#         # check palindrome
#         while rev and rev.val == slow.val:
#             slow, rev = slow.next, rev.next
#         return not rev
