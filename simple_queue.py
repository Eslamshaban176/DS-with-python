class Queue :
    class Node :
        def __init__(self, data) -> None:
            """Initializes a new Node instance."""
            self.data = data 
            self.next = None

    def __init__(self) -> None:
        """Initializes a new Queue instance."""
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self) -> bool :
        """Checks if the queue is empty or not.
        
            Args:
                - None

            Return:
                - bool
        
        """
        return self.head == None 

    def enqueue(self, data) -> None:
        """Adds a new node to the end of the queue.
            
            Args:
                - data that will be stored.

            Return:
                - None
        """
        new_node = self.Node(data)

        if self.is_empty() :
            self.head = self.tail = new_node
            self.count += 1
            return
        new_node.next = self.tail
        self.tail = new_node

        self.count += 1

    
    def dequeue(self) -> None: 
        """Removes the first node from the queue.
        
            Args:
                - None

            Return:
                - None
        """
        if self.is_empty() :
            return
        node_deleted = self.head
        self.head = self.head.next
        node_deleted.next = None

        self.count -= 1

    def peek(self) -> any: 
        """Returns the first node from the queue.
        
            Args:
                - None

            Return:
                - data 
        """
        if self.is_empty() : 
            return 
        
        return self.head
    


    def clear(self) -> None:
        """Removes all nodes from the queue.
        
            Args:
                - None

            Return:
                - None
        """
        self.head = self.tail = None


    def contains(self, data) -> bool :
        """Checks if a given data is present in the queue.

            Args:
                - The data to search for in the queue.

            Return:
                - bool
        """
        curr = self.head

        while curr :
            if curr.data == data :
                return True
            curr = curr.next

        return False
    

    def size(self) -> int : 
        """Returns the size of the queue.

            Args:
                - None

            Return:
                - Size of queue
        """
        return self.count



    def display(self) -> None: 
        """Displays the nodes in the queue.
        
            Args:
                - None

            Return:
                - None
        """
        if self.is_empty() :
            print("Queue Is Empty")
            return
        curr = self.head

        while curr != self.tail.next :
            print(curr.data , end=" -> ")
            curr = curr.next
        print()

