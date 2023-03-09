# Stack using linked List
class Stack :
    """
        Class Node - This nested class defines a node of the linked list used to implement the Stack.
                    Each node contains a data element and a reference to the next node.
        
        Methods:
            - push      - This method adds an element to the top of the Stack.
            - pop       - This method removes the top element from the Stack.
            - peek      - This method return the top element in stack.
            - is_empty  - This method to check if stack is empty or not.
            - display   - This method displays the elements of the Stack.
    """
    class Node :
        # This constructor initializes the data element of the node with the given data.
        # It also initializes the reference to the next node as None.
        def __init__(self, data) -> None:
            self.data = data
            self.next = None
            
    # This constructor initializes the Stack with the top element set to None and the size set to 0.
    def __init__(self) -> None:
        self.top = None
        self.Size = 0

    # This method to add element to the stack.
    def push(self, data):
        """
            This method adds an element to the top of the Stack.

            Args:
                - data: 
                    - The data that will be stored

            Return:
                - None

        """
        # Create a new node with the given data
        new_node = self.Node(data)

        # Check if stack is empty, set the new node as the top
        if self.is_empty() :
            self.top = new_node
        else :

            # set the link of new node to point to the top
            new_node.next = self.top

            # assign top to new_node
            self.top = new_node

        # Decreament The size of stack
        self.Size += 1

    # This method to remove the top element from the stack.
    def pop(self):
        """
            This method removes the top element from the Stack.

            Args:
                - None

            Return:
                - The data that was removed
        """
        # If the stack is empty, return None
        if self.top is None:
            return None
        else:
            # If the stack is not empty, get the top node
            popped_node = self.top
        
            # Update the top of the stack to the next node
            self.top = self.top.next
            
            # Remove the link to the popped node
            popped_node.next = None
            
            # Decrease the size of the stack
            self.Size -= 1
            
            # Return the data of the popped node
            return popped_node.data

    # This method to get the top element from the stack.
    def peek(self):
        """
            This method return the top element in stack.

            Args:
                - None.

            Return:
                - data: Any
                    Return the top element in stack
        """
        # If the stack is empty, return None
        if self.head is None:
            return None
        else:
            # Return the data of the top node
            return self.head.data

    # This method to check if stack is empty or not.
    def is_empty(self):
        return self.top is None

    # This method to search for an element in the stack.
    def search(self , data) :
        """
            This method searches for an element in the Stack.
        """
        if self.top is None :
            return False
        elif self.top.data == data :
            return True
        else :
            curr = self.top
            while curr :
                if curr.data == data :
                    return True
                curr = curr.next
        return False
    
    def display(self):
        """
            This method displays the elements of the Stack.

            Args:
                - None

            Return:
                - None
        """

        # Check if Stack is empty 
        if self.is_empty() :
            print("Stack is empty")
            return
        curr = self.top
        while curr :
            print(curr.data)
            curr = curr.next
        
