"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        temp = self.head
        if self.head:
            while temp.next:
                temp = temp.next
            temp.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        temp = self.head
        for i in range(1, position):
            if temp.value == None:
                return None
            else:
                temp = temp.next
        return temp.value
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        if position == 1:
            old = self.head
            new_element.next = old
            self.head = new_element
            return

        temp = self.head
        for i in range(1, position):
            old = temp.next
            new_element.next = old
            temp.next = new_element
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        if self.head.value == value:
            temp_next = self.head.next
            self.head = temp_next
            return

        temp = self.head
        while temp.next:
            if temp.next.value == value:
                temp_next = temp.next.next
                temp.next = temp_next
                return
            else:
                temp = temp.next

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# print(ll.head.next.next.value)
# print(ll.get_position(2).value)

ll.insert(e4, 3)
# print(ll.get_position(4).value)

ll.delete(1)
print(ll.get_position(1).value)
print(ll.get_position(2).value)
print(ll.get_position(3).value)
print(ll.get_position(4).value)