from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If inserting we must already have a tree / root
        if self.value:
            # If value is less than self.value go left, make a new tree / node if empty, otherwise
            # keep going (recursion)
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)
            # If greater than or equal to then go right, make a new tree / node if empty otherwise
            # keep going (recursion)
            elif value >= self.value:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if target == self.value, return it
        if target == self.value:
            return True
        else:
            # go left or right based on smaller or bigger
            if target < self.value:
                if self.left:
                    return self.left.contains(target)
                else:
                    return False
            elif target >= self.value:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree

    def get_max(self):
        # if right go right
        # otherwise return self.value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


temp = BinarySearchTree(3)

temp.insert(5)
temp.insert(2)
temp.insert(4)
temp.insert(11)

print(temp.value)
print(temp.left.value)
print(temp.right.value)
print(temp.right.left.value)
print(temp.contains(9))
print(temp.get_max())


def printCb(val):
    print(val)


temp.for_each(printCb)
