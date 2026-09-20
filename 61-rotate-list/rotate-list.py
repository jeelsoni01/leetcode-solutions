class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head

        curr = head
        n = 1

        while curr.next:
            curr = curr.next
            n += 1

        k %= n
        if k == 0:
            return head

        curr.next = head

        for _ in range(n - k):
            curr = curr.next

        head = curr.next
        curr.next = None

        return head