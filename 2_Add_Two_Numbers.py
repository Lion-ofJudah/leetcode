class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def give_number_from_linked_list(self, l: ListNode | None) -> int:
        result = 0
        i = 0
        
        while l is not None:
            digit_place = 1
            if i != 0:
                for _ in range(i):
                    digit_place *= 10
            
            digit = digit_place * l.val
            result += digit
            
            l = l.next 
            i += 1
        
        return result

    def give_reversed_linked_list_from_number(self, num: int) -> ListNode | None:
        init_val = num % 10
        num = num // 10
        result = ListNode(init_val)
        head = result
        while num > 0:
            val = num % 10
            result.next = ListNode(val)
            result = result.next
            num = num // 10
        
        return head

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num1 = self.give_number_from_linked_list(l1)
        num2 = self.give_number_from_linked_list(l2)
        sum = num1 + num2
        
        return self.give_reversed_linked_list_from_number(sum)

