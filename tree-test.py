https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
#from binaryTreeLinked import *
#from binaryTreeContiguous import *
from traversal import *

# these tests may not reflect those on Markus
# passing all these tests does not mean your program is correct
# we recommend making additional tests

# function to help print contiguous list
def print_contig(lst):
    for index in range(0, lst.size()):
        if lst.access(index) != None:
            print(lst.access(index), end =" ")
    print("")    


# tests without traversals
def empty_test():
    bt = BinaryTree()
    print( bt.is_empty() )

def root_print():
    bt = BinaryTree()
    bt.add_leaf(7)
    print( bt.is_empty() )
    print( bt.value(bt.get_root()) )
    
def left_print():
    bt = BinaryTree()
    bt.add_leaf(5)
    bt.add_leaf(7, bt.root(), "Left")
    print( bt.value(bt.root()) )
    print( bt.value(bt.left_child(bt.root())) )
    
def right_print():
    bt = BinaryTree()
    bt.add_leaf(5)
    bt.add_leaf(52, bt.root(), "Right")
    print( bt.value(bt.root()) )
    print( bt.value(bt.right_child(bt.root())) )    
    
# tests with traversals

def root():
    bt = BinaryTree()
    bt.add_leaf(7)
    print( bt.is_empty() )
    traversal = traverse(bt)
    print_contig(traversal)     
    
def left():
    bt = BinaryTree()
    bt.add_leaf(5)
    bt.add_leaf(7, bt.root(), "Left")
    traversal = traverse(bt)
    print_contig(traversal)

def right():
    bt = BinaryTree()
    bt.add_leaf(5)
    bt.add_leaf(7, bt.root(), "Right")
    traversal = traverse(bt)
    print_contig(traversal)
    
def twoChildren():
    bt = BinaryTree()
    bt.add_leaf(5)
    bt.add_leaf(3, bt.root(), "Right")
    bt.add_leaf(12, bt.root(), "Left")
    traversal = traverse(bt)
    print_contig(traversal)

def lefts():
    bt = BinaryTree()
    bt.add_leaf(5)
    newLeaf = bt.add_leaf(6, bt.root(), "Left")
    newLeaf = bt.add_leaf(20, newLeaf, "Left")
    newLeaf = bt.add_leaf(1, newLeaf, "Left")
    traversal = traverse(bt)
    print_contig(traversal)
    
def rights():
    bt = BinaryTree()
    bt.add_leaf(64)
    newLeaf = bt.add_leaf(16, bt.root(), "Right")
    newLeaf = bt.add_leaf(2, newLeaf, "Right")
    newLeaf = bt.add_leaf(8, newLeaf, "Right")
    traversal = traverse(bt)
    print_contig(traversal)
 
def reset():
    bt = BinaryTree()
    bt.add_leaf(5)
    bt.add_leaf(3, bt.root(), "Right")
    bt.add_leaf(12, bt.root(), "Left")
    bt.set_value(bt.root(), 72)
    traversal = traverse(bt)
    print_contig(traversal)    