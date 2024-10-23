class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        
class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node	# SET the list's head TO the node we created in the last step
        return self             # return self to allow for chaining
    
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next 	# set the runner to its neighbor
        return self	            # once the loop is done, return self to allow for chaining

    def add_to_back(self, val):
        if self.head == None:	# if the list is empty
            self.add_to_front(val)	# run the add_to_front method
            return self	# let's make sure the rest of this function doesn't happen if we add to the front
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node	# increment the runner to the next node in the list
        return self                 # return self to allow for chaining

    def remove_from_back(self):
        if self.head == None:	        # if the list is empty
            return None
        if self.head.next == None:      # If the list has only one node
            value = self.head.value
            self.head = None
            return value
        runner = self.head              # If the list has more than one node
        while (runner.next.next != None):   # Stop at the second-to-last node
            runner = runner.next
        value = runner.next.value           # Store the value of the last node
        runner.next = None                  # Remove the last node
        return self

    def remove_from_front(self):
        if self.head == None:
            return None
        value = self.head.value
        self.head = self.head.next
        return self

    def removal_val(self, val):
        if self.head is None:
            return None        
        # Case: the node with the given value is the first node
        if self.head.value == val:
            self.head = self.head.next
            return self 
        # Case: the node with the given value is the last node or in the middle
        runner = self.head
        while runner.next != None:
            if runner.next.value == val:
                runner.next = runner.next.next
            runner = runner.next
        return self

    def insert_at(self, val, n):
        new_node = SLNode(val)
        # Case: n is 0
        if n == 0:
            return self.add_to_front(val)
        runner = self.head
        current_position = 0
        while runner is not None and current_position < n-1:
            runner = runner.next
            current_position +=1
        # Case: n is larger than the length of the list
        if runner is None:
            return self.add_to_back(val)
        # Case: n is between 0 and the length of the list
        new_node.next = runner.next
        runner.next = new_node
        return self


my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").removal_val("are").insert_at("arenot", 1).print_values()    
# chaining, yeah!
# output should be:
# Linked lists
# arenot
# fun!