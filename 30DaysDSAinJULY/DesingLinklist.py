from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Modern Python 3 Dataclass for Linked List Node"""

    val: int = 0
    next: Optional["ListNode"] = None


class MyLinkedList:
    def __init__(self):
        """
        Hum ek dummy node (sentinel) se start karenge.
        Isse head par insert/delete karna bohot aasan ho jata hai.
        """
        self.head: ListNode = ListNode(0)
        self.size: int = 0

    def get(self, index: int) -> int:
        # Agar index valid nahi hai, toh -1 return karo
        if index < 0 or index >= self.size:
            return -1

        # Dummy node ke aage se traversal suru karenge
        curr = self.head.next
        for _ in range(index):
            if curr:
                curr = curr.next

        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        # Head par add karne ka matlab hai index 0 par add karna
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        # Tail par add karne ka matlab hai last size index par add karna
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        # Agar index size se bada hai, toh insert nahi karna hai
        if index > self.size:
            return

        # Discussion forum ke mutabik: agar index < 0 hai, toh use 0 treat karo
        if index < 0:
            index = 0

        # Hum us node par rukenge jo insert karne waale index se theek PEHLE (predecessor) hai
        pred: Optional[ListNode] = self.head
        for _ in range(index):
            if pred is None:
                return  # Should be unreachable due to index checks
            pred = pred.next

        if pred is None:
            return  # Should be unreachable
        # Naya node banao aur pointers link karo
        new_node = ListNode(val, pred.next)
        pred.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # Invalid index par sidhe return kar jao
        if index < 0 or index >= self.size:
            return

        # Deletion waale node se theek pehle waale node tak jao
        pred: Optional[ListNode] = self.head
        for _ in range(index):
            if pred is None:
                return  # Should be unreachable due to index checks
            pred = pred.next

        if pred is None:
            return  # Should be unreachable
        # Link ko skip karke node delete karo
        if pred.next:
            pred.next = pred.next.next
            self.size -= 1
