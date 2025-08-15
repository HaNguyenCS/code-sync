# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
        
        cur, head2 = slow, slow
        prev = None

        while cur != None:
            next_node = cur.next
            cur.next = prev
            prev, cur = cur, next_node
        head2 = prev

        while head != None and head2 != None: 
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True