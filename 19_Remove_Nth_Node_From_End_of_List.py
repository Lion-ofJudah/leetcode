class ListNode:

    def __init__(self, val:int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head == None:
            return head

        length = 0
        pointer = head
        while pointer != None:
            length += 1
            pointer = pointer.next

        pointer = head
        remove_index = length - n - 1
        i = 0
        if remove_index == -1:
            return head.next

        while pointer != None:
            if i == remove_index:
                if pointer.next != None:
                    pointer.next = pointer.next.next
                break
            i += 1
            pointer = pointer.next
        
        return head

