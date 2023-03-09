# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        count = 0

        while head:
            if isinstance(head.val, int):
                head.val = [count]
            else:
                return head
            count += 1
            head = head.next

        return head
