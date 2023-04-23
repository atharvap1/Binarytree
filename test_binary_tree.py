import unittest
from binary_tree import BinaryTree  # Import the BinaryTree class from binary_tree module

class TestBinaryTree(unittest.TestCase):  # Define a test case class that extends unittest.TestCase
    def setUp(self):  # Define a setup method that is called before each test
        self.tree = BinaryTree()  # Create an instance of BinaryTree for each test

    def test_insert(self):  # Define a test method for the insert method of BinaryTree
        self.tree.insert(5)  # Insert node with data 5 into the tree
        self.tree.insert(3)  # Insert node with data 3 into the tree
        self.tree.insert(7)  # Insert node with data 7 into the tree
        self.assertEqual(self.tree.root.data, 5)  # Check that the root node's data is 5
        self.assertEqual(self.tree.root.left.data, 3)  # Check that the left child of the root node's data is 3
        self.assertEqual(self.tree.root.right.data, 7)  # Check that the right child of the root node's data is 7

    def test_find(self):  # Define a test method for the find method of BinaryTree
        self.tree.insert(5)  # Insert node with data 5 into the tree
        self.tree.insert(3)  # Insert node with data 3 into the tree
        self.tree.insert(7)  # Insert node with data 7 into the tree
        self.assertTrue(self.tree.find(5))  # Check that the tree contains a node with data 5
        self.assertTrue(self.tree.find(3))  # Check that the tree contains a node with data 3
        self.assertTrue(self.tree.find(7))  # Check that the tree contains a node with data 7
        self.assertFalse(self.tree.find(10))  # Check that the tree does not contain a node with data 10

    def test_delete(self):  # Define a test method for the delete method of BinaryTree
        self.tree.insert(5)  # Insert node with data 5 into the tree
        self.tree.insert(3)  # Insert node with data 3 into the tree
        self.tree.insert(7)  # Insert node with data 7 into the tree
        self.tree.delete(7)  # Delete node with data 7 from the tree
        self.assertFalse(self.tree.find(7))  # Check that the tree no longer contains a node with data 7

    def test_preorder_traversal(self):  # Define a test method for the _preorder_traversal method of BinaryTree
        self.tree.insert(5)  # Insert node with data 5 into the tree
        self.tree.insert(3)  # Insert node with data 3 into the tree
        self.tree.insert(7)  # Insert node with data 7 into the tree
        expected_output = [5, 3, 7]  # Define the expected output of the preorder traversal
        output = []  # Define an empty list to store the actual output of the preorder traversal
        def print_node_data(data):  # Define a helper function to append the data of each node to the output list
            output.append(data)
        self.tree._preorder_traversal(self.tree.root, print_node_data)  # Call the _preorder_traversal method with the root node and the helper function
        self.assertEqual(output, expected_output)  # Check that the actual output matches the expected output


    # Define a test method for inorder traversal
    def test_inorder_traversal(self):
        # Create a binary search tree and insert some nodes
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        # Define the expected output and an empty list to store the output
        expected_output = [3, 5, 7]
        output = []
        # Define a callback function to append each node's data to the output list
        def print_node_data(data):
            output.append(data)
        # Perform the inorder traversal and check that the output matches the expected output
        self.tree._inorder_traversal(self.tree.root, print_node_data)
        self.assertEqual(output, expected_output)

    # Define a test method for postorder traversal
    def test_postorder_traversal(self):
        # Create a binary search tree and insert some nodes
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        # Define the expected output and an empty list to store the output
        expected_output = [3, 7, 5]
        output = []
        # Define a callback function to append each node's data to the output list
        def print_node_data(data):
            output.append(data)
        # Perform the postorder traversal and check that the output matches the expected output
        self.tree._postorder_traversal(self.tree.root, print_node_data)
        self.assertEqual(output, expected_output)

    # Define a test method for finding the maximum depth of the tree
    def test_max_depth(self):
        # Create a binary search tree and insert some nodes
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(8)
        # Check that the maximum depth of the tree is 3
        self.assertEqual(self.tree.max_depth(self.tree.root), 3)

    # Define a test method for level-order traversal
    def test_level_order_traversal(self):
        # Create a binary search tree and insert some nodes
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        # Define the expected output
        expected_output = [[5], [3, 7]]
        # Check that the level-order traversal matches the expected output
        self.assertEqual(self.tree.level_order_traversal(), expected_output)

    # Define a test method for finding the maximum path sum
    def test_max_path_sum(self):
        # Create a binary search tree and insert some nodes
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.insert(3)
        # Check that the maximum path sum is 6
        self.assertEqual(self.tree.max_path_sum(), 6)

if __name__ == '__main__':
    # Run the tests
    unittest.main()
