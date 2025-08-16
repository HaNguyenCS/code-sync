# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        dum = ListNode(0, head)
        prev = head
        while cur:
            if cur.val == val:
                if dum.next.val == val:
                    dum.next = cur.next
                    prev = cur
                else:
                    prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return dum.next