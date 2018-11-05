#4. Modify the code for a binary search tree to make it threaded. Write a non-recursive inorder traversal method 
# for the threaded binary search tree. A threaded binary tree maintains a reference from each node to its successor.
import module_bin_search_tree as bst
import threading

class ThreadedTraversalLeft(threading.Thread):
    def __init__(self, tree, threadID, name, counter):
        threading.Thread.__init__(self)
        self.tree = tree
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        self.print_nodes(self.tree.root.left_child)

    def print_nodes(self, node):
        if node is not None:
            print(node.payload)
            self.print_nodes(node.left_child)
            self.print_nodes(node.right_child)
        
class ThreadedTraversalRight(threading.Thread):
    def __init__(self, tree, threadID, name, counter):
        threading.Thread.__init__(self)
        self.tree = tree
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        self.print_nodes(self.tree.root.right_child)

    def print_nodes(self, node):
        if node is not None:
            print(node.payload)
            self.print_nodes(node.left_child)
            self.print_nodes(node.right_child)        

def print_tree_threaded(tree):
    print(tree.root.payload)
    thread_left_branch = ThreadedTraversalLeft(tree, 1, "ThreadLeft", 1)
    thread_right_branch = ThreadedTraversalRight(tree, 2, "ThreadRight", 2)
    thread_left_branch.start()
    thread_right_branch.start()

r = bst.BinarySearchTree()
r[1] = 1
r[3] = 54
r[9] = 4
r[23] = 'hello'
print_tree_threaded(r)