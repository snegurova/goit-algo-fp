"""Module providing a class implementing linked list."""
class Node:
    """Class implementing node of linked list"""
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """Class implementing linked list"""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Function implementing insert into beginning of the linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Function implementing insert into the end of the linked list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        """Function implementing insert after node of linked list"""
        if prev_node is None:
            print("Previous node doesn't exists.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        """Function implementing deleting node of the linked list"""
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        """Function implementing search element of the linked list"""
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse(self):
        """Function implementing linked list reversing"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_insert(self, new_node):
        """Function implementing sorted insert"""
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insertion_sort(self):
        """Function implementing insertion sort"""
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            sorted_list.sorted_insert(current)
            current = next_node
        self.head = sorted_list.head

    def print_list(self):
        """Function implementing linked list printing"""
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def merge_sorted(self, other):
        """Function implementing merge of sorted lists"""
        merged_list = LinkedList()
        p1 = self.head
        p2 = other.head

        if not p1:
            merged_list.head = p2
            return merged_list
        if not p2:
            merged_list.head = p1
            return merged_list

        if p1.data <= p2.data:
            merged_list.head = p1
            p1 = p1.next
        else:
            merged_list.head = p2
            p2 = p2.next

        current = merged_list.head
        while p1 and p2:
            if p1.data <= p2.data:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next

        if p1:
            current.next = p1
        if p2:
            current.next = p2

        return merged_list

if __name__ == "__main__":

    # Creating first list
    llist1 = LinkedList()
    llist1.insert_at_end(1)
    llist1.insert_at_end(3)
    llist1.insert_at_end(5)

    # Creating second list
    llist2 = LinkedList()
    llist2.insert_at_end(2)
    llist2.insert_at_end(4)
    llist2.insert_at_end(6)

    # Merging of sorted lists
    merged_list = llist1.merge_sorted(llist2)

    # Printing of merged list
    print("Merged sorted list:")
    merged_list.print_list()

    # List reversing
    llist1.reverse()
    print("\nReversed order of the first list:")
    llist1.print_list()

    # Insertion sort
    llist1.insert_at_end(4)
    llist1.insert_at_end(2)
    llist1.insert_at_end(7)
    llist1.insertion_sort()
    print("\nFirst lits after insertion sort:")
    llist1.print_list()
