# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        position = 1
        
        first_critical = -1
        prev_critical = -1
        min_distance = float('inf')

        while curr and curr.next:
            nxt = curr.next

     
            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):

                if first_critical == -1:
                    first_critical = position
                else:
                    min_distance = min(
                        min_distance,
                        position - prev_critical
                    )

                prev_critical = position

            prev = curr
            curr = curr.next
            position += 1

        
        if first_critical == -1 or first_critical == prev_critical:
            return [-1, -1]

        max_distance = prev_critical - first_critical

        return [min_distance, max_distance]