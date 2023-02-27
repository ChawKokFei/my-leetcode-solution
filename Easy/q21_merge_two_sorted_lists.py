class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        print(list1)
        if list1 != None or list2 != None:
            newList = ListNode()
            finalList = newList
        else:
            return

        while list1 != None or list2 != None:
            if list1 != None and list2 != None:
                if list1.val <= list2.val:
                    newList.val = list1.val
                    list1 = list1.next
                    if list1 != None or list2 != None:
                        newList.next = ListNode()
                        newList = newList.next
                    continue

                else:
                    newList.val = list2.val
                    list2 = list2.next
                    if list1 != None or list2 != None:
                        newList.next = ListNode()
                        newList = newList.next
                    continue

            if list1 != None and list2 == None:
                newList.val = list1.val
                list1 = list1.next
                if list1 != None or list2 != None:
                    newList.next = ListNode()
                    newList = newList.next
                continue

            if list2 != None and list1 == None:
                newList.val = list2.val
                list2 = list2.next
                if list1 != None or list2 != None:
                    newList.next = ListNode()
                    newList = newList.next
                continue

        return finalList


solution = Solution()
solution.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4, None))), ListNode(
    1, ListNode(3, ListNode(4, None))))
