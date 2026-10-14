class ListNode:

    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head == None or head.next == None:
            return head
        
        pp = None
        p = head
        c = head.next
        rh = c

        while c != None:
            p.next = c.next
            c.next = p
            pp = p
            p = p.next

            if p == None or p.next == None:
                break

            c = p.next
            pp.next = c

        return rh

