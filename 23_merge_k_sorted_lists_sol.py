# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # using heapq -> Min Heap
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]: # root of the linked list
                # cannot push the duplicate values
                # push the value with i and lists[i]
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            # pop the min value from the heap
            node = heapq.heappop(heap)
            idx = node[1] # index of the node
            result.next = node[2] # next nodes of the node

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        return root.next
