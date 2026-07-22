class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            first, second = head, head.next
            prev.next, first.next, second.next = second, second.next, first
            prev, head = first, first.next
        return dummy.next

        