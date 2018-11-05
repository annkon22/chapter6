#7. Clean up the print_expfunction so that it does not include an ‘extra’ set of parentheses around each number.
class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

def print_exp(tree):
    str_val = ""
    if tree:
        str_val = ' ' + print_exp(tree.get_left_child())
        str_val = str_val + str(tree.get_root_val())
        str_val = str_val + print_exp(tree.get_right_child()) + ' '
    return str_val

r = BinaryTree(3)
r.insert_left('+')
r.insert_left(6)
r.insert_left(20)
r.insert_left('+')
print(print_exp(r))