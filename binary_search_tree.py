class BinarySearchTree:
    def __init__(self, value, depth=1):
        """The __init__ method creates a tree node. The default depth of
        1 equates to the root node.

        Args:
            value (_type_): The value of the node to be added. Can be of
            any type.
            depth (int, optional): How deep the node is in the tree.
            Defaults to 1.
        """

        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        """Method to insert a new node in the tree.

        Args:
            value (_type_): The value for the new node.
        """

        # Add the new node to the left
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value, self.depth + 1)
                print(
                    f"Tree node {value} added to the left of {self.value} at depth "
                    f"{self.depth + 1}"
                )
            else:
                self.left.insert(value)

        # Add the new node to the right
        else:
            if self.right is None:
                self.right = BinarySearchTree(value, self.depth + 1)
                print(
                    f"Tree node {value} added to the right of {self.value} at depth "
                    f"{self.depth + 1}"
                )
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        """Method to find a node with given value.

        Args:
            value (_type_): The value of the node to find in the tree.

        Returns:
            _type_: The node that is found
        """
        if self.value == value:
            return self
        elif (self.left is not None) and (value < self.value):
            return self.left.get_node_by_value(value)
        elif (self.right is not None) and (value >= self.value):
            return self.right.get_node_by_value(value)
        else:
            return None

    def find_minimum_value_node(self):
        """Finds the minimum value node in a tree.

        Returns:
            _type_: The node with the minimum value
        """
        current = self.value
        while self.left is not None:
            current = current.left
        return current

    def delete(self, value):
        """Method to remove a node from the tree.

        Args:
            value (_type_): The value of the node to remove.
        """

        # Base case
        if self == None:
            return self

        # If value is less than root value
        if value < self.value:
            self.left = self.left.delete(value)

        # If value is greater than the root value
        elif value > self.value:
            self.right = self.right.delete(value)

        # If the root value is the value to be deleted
        else:
            # If it has no children or one child
            if self.left is None:
                temp = self.right
                self = None
                return temp

            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # A node with two children
            temp = self.right.find_minimum_value_node()
            self.value = temp.value
            self.right.delete(temp)

        return self

    def depth_first_traversal(self):
        """Print the inorder traversal of the Binary Serach Tree."""
        if self.left is not None:
            self.left.depth_first_traversal()
        print(f"Depth={self.depth}, Value={self.value}")

        if self.right is not None:
            self.right.depth_first_traversal()


# For Testing
print("Creating Binary Search Tree rooted at value 15:")
tree = BinarySearchTree(15)

items = [8, 4, 10, 7, 1, 12, 30, 20, 50, 43, 26]
for item in items:
    tree.insert(item)

print("Printing the inorder depth-first traversal:")
tree.depth_first_traversal()
item_to_delete = 7
tree.delete(item_to_delete)
print(f"Printing the inorder depth-first traversal with {item_to_delete} removed:")
tree.depth_first_traversal()
