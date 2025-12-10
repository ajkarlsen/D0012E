from main import *
from treedraw import *
import random
import time


def generateSorted(tree, n):
    for i in range(n):
        tree.insert_value(i)
    return tree

def generateReverse(tree, n):
    for i in range(n, 0, -1):
        tree.insert_value(i)
    return tree

def generate_tree(tree,n):
    for i in range(n):
        tree.insert_value(random.randint(0, n))
    return tree

def analyse(tree, function, n):
    start = time.time()
    tree= function(tree,n)
    height = tree.get_height(tree.root)
    end = time.time()
    print(f"Number of rotations: {tree.rotations}")
    print(f"Running time: {end - start}")
    print(f"Height of tree: {height}")
    return tree

start_node = Treenode(0)
tree = AVLTree(start_node, 1)
tree = analyse(tree, generate_tree, 500000)
#display(tree.root)
print()
tree2 = AVLTree(start_node, 3)
tree2 = analyse(tree2, generate_tree, 500000)