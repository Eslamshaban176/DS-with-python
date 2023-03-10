# SLL => Singly LinkedList
class SLL :
    """
        SLL: Singly LinkedList contains the following methods:

        Node - a nested class representing the nodes of the linked list. Each node contains data and a reference (next_node) to the next node in the sequence.

        __init__ - the constructor method that initializes the head, tail, and size of the linked list.

        prepend - adds a new node with the specified data to the beginning of the linked list.

        append - adds a new node with the specified data to the end of the linked list.

        Insert - inserts a new node with the given data at the specified position.

        search - searches for a node with the specified data in the linked list. If the node is found, it returns True, otherwise it returns False.

        delete - removes the node with the specified data from the linked list.

        length - returns the number of nodes in the linked list.

        display - prints the contents of the linked list.

    """
    class Node :
        def __init__( self , data , next_node = None) :
            self.data = data
            self.next_node = next_node

    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, data) -> None:
        """
            Adds a new node with the specified data to the beginning of the linked list.

            Args:
                data: Any
                    The data to be stored in the new node.

            Returns:
                - None

        """ 
        # Create a new node with the given data        
        new_node = self.Node(data)
        # If the linked list is empty, set the new node as the head
        if self.head is None :
            self.head = new_node
        else:
            # Set the new node as the head's next node
            new_node.next_node = self.head
            self.head = new_node
        # Increment the size of the linked list
        self.size += 1    

    def append(self, data) -> None:
        """
            Adds a new node with the specified data to the end of the linked list.

            Args:
                data: Any
                    The data to be stored in the new node.

            Returns:
                - None

        """   
        # Create a new node with the given data      
        new_node = self.Node(data)
        # If the linked list is empty, set the new node as the head
        if self.head is None :
            self.head = new_node
        else:
            # Set the new node as the tail's next node
            curr = self.head
            while curr.next_node :
                curr = curr.next_node

            curr.next_node = new_node
        # Increament the size of the linked list
        self.size += 1    

    def insert(self, data, pos = -1):
        """
        Insert a new node with the given data at the specified position.
        If the position is not specified, the node will be added at the end of the list.

        Args:
            - data: the data to be stored in the new node.
            - pos (optional): the position where the new node should be inserted.

        Returns:
            - None

        Raises:
            If the list is shorter than the specified position, raise an error

        """
        # Create a new node with the given data
        new_node = self.Node(data)
        
        # If position is 0, insert the new node at the beginning of the list
        if pos == 0 or self.head is None:
            self.prepend(data)
        elif pos == -1 :
            self.append(data)
        else:
            if pos < 0 :
                pos = self.length() + pos 

            # Traverse the list to find the node at the specified position
            curr = self.head

            for _ in range(pos-1):
                if curr.next_node is None:
                    # If the list is shorter than the specified position, raise an error
                    raise IndexError("Position out of range")
                curr = curr.next_node
            
            # Insert the new node after the current node
            new_node.next_node = curr.next_node
            curr.next_node = new_node
            # Increament the size of the linked list
            self.size += 1

    def search(self, data) -> bool:
        """
            Searches for a node with the specified data in the linked list

            Args:
                data: Any
                    The data to search for in the linked list.

            Returns:
                bool:
                    True if a node containing the given `data` value is found in the linked list, 
                    False otherwise.
        """
        # If the linked list is empty, return False        
        if self.head is None :
            return False
        # Start at the head of the linked list
        cur = self.head
        while cur:
            # If the current node contains the given data, return True
            if cur.data == data :
                return True
            # Otherwise, move to the next node in the list
            cur = cur.next_node
        # If the end of the list is reached without finding the data, return False
        return False

    def delete(self , data) -> None:
        """
            Removes the node containing the specified data from the linked list.

            Args:
                data: Any
                    The data to be removed.

            Returns:
                - None

        """
        # Check if the list is empty
        if self.head is None :
            return 
        # Check if the head node is the node to be deleted
        elif self.head.data == data :
            self.head = self.head.next_node
        else :
            # Iterate over the list to find the node to be deleted
            cur = self.head
            while cur.next_node :
                if cur.next_node.data == data :
                    cur.next_node = cur.next_node.next_node
                    return
                cur = cur.next_node
        # Decreament the size of the linked list
        self.size -= 1
                    
    def length(self) -> int:
        """
            return the length of the linked list.

            Args:
                None

            Returns:
                number: 
                    The number of nodes in linked list.
        """  
        return self.size


    def display(self):
        """
            Prints the contents of the linked list.

            Args:
                - None

            Returns:
                - None

        """    
        # Check if list is empty , print "List is Empty"
        if self.head is None :
            print("List is Empty")
            return
        # Iterate over the list to print each the node of data 
        cur_node = self.head   
        while cur_node:
            print(cur_node.data , end = " -> ")   
            cur_node = cur_node.next_node 
        print("Null")

