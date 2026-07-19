from typing import Optional

"""
QUESTION: Implement a Singly Linked List in Python from scratch. 
Cover all operations: Node Creation, Insertion (Start, End, Middle), 
Deletion (All Corner Cases), and Traversal/Display.
"""


class Node:
    def __init__(self, data):
        self.data = data  # Data Part: Actual value store karne ke liye
        self.next: Optional["Node"] = None  # Next Part: Agle node ka memory address rakhne ke liye


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None  # Head Pointer: Hamesha list ke starting node ka address hold karta hai

    def insert_at_start(self, data):
        new_node = Node(data)  # Naya block/node banaya
        new_node.next = self.head  # Naye node ko purane head se connect kiya
        self.head = new_node  # Head ko shift karke naye node par set kiya

    def insert_at_end(self, data):
        new_node = Node(data)  # Naya block/node banaya
        if not self.head:
            self.head = new_node
            return  # Corner Case: Agar list khali ho
        temp = self.head  # Assistant pointer 'temp' ko shuruat me rakha
        while temp and temp.next:  # Loop chala kar aakhiri node tak pahuche
            temp = temp.next
        temp.next = new_node  # Last node ke next part me naya node jod diya

    def insert_after(self, target, data):
        temp = self.head  # Head se search shuru kiya
        while temp and temp.data != target:
            temp = temp.next  # Target value dhoodhi
        if temp:  # Agar target node mil gaya to:
            new_node = Node(data)  # Naya node banaya
            new_node.next = temp.next  # Naye node ko target ke agle wale node se joda
            temp.next = new_node  # Target node ko naye node se link kiya

    def delete_node(self, value):
        curr: Optional[Node] = self.head
        prev: Optional[Node] = None

        if curr and curr.data == value:
            self.head = curr.next
            return

        while curr and curr.data != value:
            prev = curr
            curr = curr.next

        if curr and prev:  # if curr is not None (node to delete found) AND it's not the head
            prev.next = curr.next

    def display(self):
        temp = self.head  # Assistant pointer ko start me rakha
        while temp:  # Jab tak list ke end (None) tak nahi pahunchte
            print(temp.data, end=" -> ")
            temp = temp.next  # Data print kiya aur aage badhe
        print("None")  # End show karne ke liye last me None print kiya


# --- Driver Code for Codesnap Testing ---
ll = LinkedList()
ll.insert_at_end(10)  # List ban gayi: 10 -> None
ll.insert_at_start(5)  # Shuru me joda: 5 -> 10 -> None
ll.insert_at_end(20)  # End me joda: 5 -> 10 -> 20 -> None
ll.insert_after(10, 15)  # 10 ke baad joda: 5 -> 10 -> 15 -> 20 -> None
ll.delete_node(10)  # 10 ko delete kiya: 5 -> 15 -> 20 -> None
ll.display()  # Final Output Screen pe print hoga

"""
QUICK SUMMARY:
1. Node Structure: Har ek block ke paas do chize hoti hain—Data aur agle node ka Address (Next).
2. Head Pointer: Yeh list ka entry gate hai. Isko bina soche-samjhe aage nahi badhate varna piche ka address kho jata hai.
3. Temp/Assistant Pointer: Puri list me aage ghumne (Traversing) ke liye hamesha 'temp' ka use karte hain.
4. Dynamic Size: Array ki tarah iska size fixed nahi hota, run-time par memory blocks judte ya toot-te rehte hain.
5. One-Way Chain: Singly Linked List me hum sirf aage ja sakte hain, piche mudne ka koi rasta nahi hota.
"""
