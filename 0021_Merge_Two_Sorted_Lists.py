class ListNode:

    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        list_node: ListNode | None = None
        if list1.val <= list2.val:
            list_node = ListNode(list1.val)
            list1 = list1.next
        else:
            list_node = ListNode(list2.val)
            list2 = list2.next
        head = list_node

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                list_node.next = list1
                list1 = list1.next
            else:
                list_node = list2
                list2 = list2.next

            list_node = list_node.next

        if list1 != None:
            list_node.next = list1
        elif list2 != None:
            list_node.next = list2

        return head

