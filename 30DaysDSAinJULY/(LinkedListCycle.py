from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val: int = x
        self.next: Optional['ListNode'] = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Do pointers initialize kiye type hinting ke sath
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head
        
        # Jab tak fast pointer ya uske aage ka node None nahi hota
        while fast and fast.next:
            assert slow is not None  # Help Pylance understand `slow` can't be None here
            slow = slow.next         # 1 step aage
            fast = fast.next.next    # 2 steps aage
            
            # Agar dono pointers meet karte hain, matlab cycle hai
            if slow == fast:
                return True
                
        # Agar loop se bahar aa gaye, matlab list ka end mil gaya (No Cycle)
        return False