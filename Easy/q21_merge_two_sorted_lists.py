class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # if list1 != None or list2 != None:
        #     newList = ListNode()
        #     finalList = newList
        # else:
        #     return

        # while list1 != None or list2 != None:
        #     if list1 != None and list2 != None:
        #         if list1.val <= list2.val:
        #             newList.val = list1.val
        #             list1 = list1.next
        #             if list1 != None or list2 != None:
        #                 newList.next = ListNode()
        #                 newList = newList.next
        #             continue

        #         else:
        #             newList.val = list2.val
        #             list2 = list2.next
        #             if list1 != None or list2 != None:
        #                 newList.next = ListNode()
        #                 newList = newList.next
        #             continue

        #     if list1 != None and list2 == None:
        #         newList.val = list1.val
        #         list1 = list1.next
        #         if list1 != None or list2 != None:
        #             newList.next = ListNode()
        #             newList = newList.next
        #         continue

        #     if list2 != None and list1 == None:
        #         newList.val = list2.val
        #         list2 = list2.next
        #         if list1 != None or list2 != None:
        #             newList.next = ListNode()
        #             newList = newList.next
        #         continue

        # return finalList

        # Alternate solution by https://leetcode.com/artod/
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


solution = Solution()
solution.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4, None))), ListNode(
    1, ListNode(3, ListNode(4, None))))
