from ast import List
import collections
from node import Node

# Define a class for binary trees
class BinaryTree:
    # Constructor to initialize the root node to None
    def __init__(self):
        self.root = None

    # Function to insert a node with a given data value into the binary tree
    def insert(self, data):
        # If the root node is None, create a new node with the given data value and set it as the root
        if not self.root:
            self.root = Node(data)
        # Otherwise, recursively insert the node into the appropriate subtree
        else:
            self._insert(data, self.root)

    # Helper function for the insert method
    def _insert(self, data, current_node):
        # If the data value is less than the current node's data value, insert it into the left subtree
        if data < current_node.data:
            # If the left child is None, create a new node with the given data value and set it as the left child
            if not current_node.left:
                current_node.left = Node(data)
            # Otherwise, recursively insert the node into the left subtree
            else:
                self._insert(data, current_node.left)
        # If the data value is greater than the current node's data value, insert it into the right subtree
        elif data > current_node.data:
            # If the right child is None, create a new node with the given data value and set it as the right child
            if not current_node.right:
                current_node.right = Node(data)
            # Otherwise, recursively insert the node into the right subtree
            else:
                self._insert(data, current_node.right)

    # Function to find a node with a given data value in the binary tree
    def find(self, data):
        # If the root node is None, the tree is empty and the node cannot be found
        if not self.root:
            return False
        # Otherwise, recursively search for the node
        else:
            return self._find(data, self.root)

    # Helper function for the find method
    def _find(self, data, current_node):
        # If the data value matches the current node's data value, the node has been found
        if data == current_node.data:
            return True
        # If the data value is less than the current node's data value, search the left subtree
        elif data < current_node.data and current_node.left:
            return self._find(data, current_node.left)
        # If the data value is greater than the current node's data value, search the right subtree
        elif data > current_node.data and current_node.right:
            return self._find(data, current_node.right)
        # If the node cannot be found in the subtree, return False
        return False

    # Function to delete a node with a given data value from the binary tree
    def delete(self, data):
        # Call the helper function with the root node and the data value to be deleted
        self.root = self._delete(self.root, data)

    # Helper function for the delete method
    def _delete(self, current_node, data):
        # If the current node is None, the data value cannot be found and the tree remains unchanged
        if not current_node:
            return current_node
        # If the data value is less than the current node's data value, delete the node from the left subtree
        elif data < current_node.data:
            current_node.left = self._delete(current_node.left, data)
        # If the data value is greater than the current node's data value, delete the node from the right subtree
        elif data > current_node.data:
            current_node.right = self._delete(current_node.right, data)
        else:
            # If the current node has no left child, return its right child as the new subtree
            if not current_node.left:
                return current_node.right
            # If the current node has no right child, return its left child as the new subtree
            elif not current_node.right:
                return current_node.left
            else:
                # If the current node has both left and right children, find the minimum node in the right subtree
                # Replace the current node's data with the minimum node's data
                # Recursively delete the minimum node from the right subtree
                min_node = self._find_min(current_node.right)
                current_node.data = min_node.data
                current_node.right = self._delete(current_node.right, min_node.data)
        # Return the updated subtree
        return current_node

# Function to find minimum value a node with a given data value from the binary tree
    def _find_min(self, current_node):
        # Keep traversing to the left subtree until we find a leaf node (i.e., a node with no left child)
        while current_node.left:
            current_node = current_node.left
        # Return the leaf node, which will have the smallest value in the subtree
        return current_node

# Function to find traverse the tree in a pre-order manner with a given data value from the binary tree
    def preorder_traversal(self, callback):
        # Wrapper method for the recursive preorder traversal
        self._preorder_traversal(self.root, callback)

    def _preorder_traversal(self, current_node, callback):
        if current_node:
            # Perform the callback on the current node's data
            callback(current_node.data)
            # Recursively traverse the left subtree
            self._preorder_traversal(current_node.left, callback)
            # Recursively traverse the right subtree
            self._preorder_traversal(current_node.right, callback)

# Function to find inorder traversal of the binary search tree with a given data value from the binary tree
    def inorder_traversal(self, callback):
        # Wrapper method for the recursive inorder traversal
        self._inorder_traversal(self.root, callback)

    def _inorder_traversal(self, current_node, callback):
        if current_node:
            # Recursively traverse the left subtree
            self._inorder_traversal(current_node.left, callback)
            # Perform the callback on the current node's data
            callback(current_node.data)
            # Recursively traverse the right subtree
            self._inorder_traversal(current_node.right, callback)
# Function to find postorder traversal of the binary search tree with a given data value from the binary tree
    def postorder_traversal(self, callback):
        # Wrapper method for the recursive postorder traversal
        self._postorder_traversal(self.root, callback)

    def _postorder_traversal(self, current_node, callback):
        if current_node:
            # Recursively traverse the left subtree
            self._postorder_traversal(current_node.left, callback)
            # Recursively traverse the right subtree
            self._postorder_traversal(current_node.right, callback)
            # Perform the callback on the current node's data
            callback(current_node.data)

# Function to find maximum depth of the binary tree with a given data value from the binary tree
    def max_depth(self, node):
        if not node:
            # Base case: the current node is None, so its height is 0
            return 0
        else:
            # Recursively compute the maximum height of the left and right subtrees
            left_height = self.max_depth(node.left)
            right_height = self.max_depth(node.right)
            # Return the maximum height of the left and right subtrees, plus one for the root node
            return max(left_height, right_height) + 1

# Function to find level order traversal of the binary tree with a given data value from the binary tree
    def level_order_traversal(self):
        result = []
        if not self.root:
            # Base case: the tree is empty, so return an empty list
            return result
        # Use a queue to perform a level order traversal
        queue = collections.deque([self.root])
        while queue:
            level_result = []
            level_size = len(queue)
            # Process all nodes at the current level before moving on to the next level
            for i in range(level_size):
                node = queue.popleft()
                # Add the current node's data to the level result list
                level_result.append(node.data)
                # Add the current node's children to the queue (if they exist)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Add the level result list to the final result list
            result.append(level_result)
        # Return the final result list of level order traversal
        return result

# Function to find maximum path sum of the binary tree with a given data value from the binary tree
    def max_path_sum(self):
        # If the root node is None, return 0 as there is no path
        if not self.root:
            return 0

        # Initialize max_sum with the smallest possible value
        max_sum = float('-inf')

        # Define a nested function dfs to traverse the tree and calculate the maximum path sum
        def dfs(node):
            nonlocal max_sum
            
            # If the current node is None, return 0 to avoid negative values
            if not node:
                return 0
            
            # Calculate the maximum path sum in the left and right subtrees
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            
            # Update the max_sum if the current path has a greater sum
            max_sum = max(max_sum, left + right + node.data)
            
            # Return the maximum path sum of the current subtree, which can be either left or right path + node.data
            return max(left, right) + node.data

        # Start the dfs from the root node
        dfs(self.root)

        # Return the maximum path sum
        return max_sum


    