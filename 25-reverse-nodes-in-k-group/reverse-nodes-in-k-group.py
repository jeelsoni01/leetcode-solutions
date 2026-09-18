class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        prev = dummy

        while True:
            curr = prev
            for _ in range(k):
                curr = curr.next
                if not curr:
                    return dummy.next

            tail = prev.next
            curr = tail.next

            for _ in range(k - 1):
                tail.next = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = tail.next

            prev = tail