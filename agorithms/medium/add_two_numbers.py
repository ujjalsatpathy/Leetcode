from typing import Optional


# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        empty_node = ListNode()
        current_node = empty_node
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry, digit = divmod(total, 10)
            current_node.next = ListNode(digit)
            current_node = current_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return empty_node.next
