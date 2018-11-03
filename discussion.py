#1. 
import module_stack as s
import operator

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

def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    p_stack = s.Stack()
    e_tree = BinaryTree('')
    p_stack.add(e_tree)
    current_tree = e_tree
    for i in fp_list:
        if i == '(':
            current_tree.insert_left('')
            p_stack.add(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_val(int(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.add(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree


my_exp = '( 4 * 8 ) / 6 - 3'
build_parse_tree(my_exp)

#2. Consider the following list of integers: [1,2,3,4,5,6,7,8,9,10]. 
# Show the binary search tree resulting from inserting the integers in the list.
### Binary Search Trees

class TreeNode: 
    def __init__(self, key, val, left = None, right = None, parent = None): 
        self.key = key
        self.payload = val 
        self.left_child = left 
        self.right_child = right 
        self.parent = parent

    def has_left_child(self): 
        return self.left_child

    def has_right_child(self): 
        return self.right_child

    def is_left_child(self): 
        return self.parent and self.parent.left_child == self

    def is_right_child(self): 
        return self.parent and self.parent.right_child == self

    def is_root(self): 
        return not self.parent


    def is_leaf(self): 
        return not (self.right_child or self.left_child)

    def has_any_children(self): 
        return self.right_child or self.left_child

    def has_both_children(self): 
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, lc, rc): 
        self.key = key 
        self.payload = value 
        self.left_child = lc 
        self.right_child = rc 
        if self.has_left_child(): 
            self.left_child.parent = self 
        if self.has_right_child(): 
            self.right_child.parent = self
    
    def splice_out(self):
        if self.is_leaf(): 
            if self.is_left_child(): 
                self.parent.left_child = None 
            else: self.parent.right_child = None 
        elif self.has_any_children(): 
            if self.has_left_child(): 
                if self.is_left_child(): 
                    self.parent.left_child = self.left_child 
                else: 
                    self.parent.right_child = self.left_child 
            self.left_child.parent = self.parent 
        else: 
            if self.is_left_child(): 
                self.parent.left_child = self.right_child 
            else: 
                self.parent.right_child = self.right_child 
            self.right_child.parent = self.parent

    def find_successor(self): 
        succ = None 
        if self.has_right_child(): 
            succ = self.right_child.find_min() 
        else: 
            if self.parent: 
                if self.is_left_child(): 
                    succ = self.parent 
                else: self.parent.right_child = None 
                succ = self.parent.find_successor() 
                self.parent.right_child = self 
        return succ

    def find_min(self): 
        current = self 
        while current.has_left_child(): 
            current = current.left_child 
        return current

class BinarySearchTree: 
    def __init__(self): 
        self.root = None 
        self.size = 0

    def length(self): 
        return self.size

    def __len__(self): 
        return self.size

    def put(self, key, val): 
        if self.root: 
            self._put(key, val, self.root) 
        else: 
            self.root = TreeNode(key,val) 
            self.size = self.size + 1

    def _put(self, key, val, current_node): 
        if key < current_node.key: 
            if current_node.has_left_child(): 
                self._put(key, val, current_node.left_child) 
            else: current_node.left_child = TreeNode(key, val, parent = current_node) 
        else: 
            if current_node.has_right_child(): 
                self._put(key, val, current_node.right_child) 
            else: current_node.right_child = TreeNode(key, val, parent = current_node)

    def __setitem__(self, k, v): 
        self.put(k, v)

    def get(self, key): 
        if self.root: 
            res = self._get(key, self.root) 
            if res: 
                return res.payload 
            else: 
                return None 
        else: return None

    def _get(self, key, current_node): 
        if not current_node: 
            return None 
        elif current_node.key == key: 
            return current_node 
        elif key < current_node.key: 
            return self._get(key, current_node.left_child) 
        else: 
            return self._get(key, current_node.right_child)

    def __getitem__(self, key): 
        return self.get(key)

    def __contains__(self, key): 
        if self._get(key, self.root): 
            return True 
        else: return False

    def delete(self, key): 
        if self.size > 1: 
            node_to_remove = self._get(key, self.root) 
            if node_to_remove: 
                self.remove(node_to_remove) 
                self.size = self.size - 1 
            else: raise KeyError('Error, key not in tree') 
        elif self.size == 1 and self.root.key == key: 
            self.root = None 
            self.size = self.size - 1 
        else: 
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key): 
        self.delete(key)
        


    def remove(self, current_node): 
        if current_node.is_leaf():  
            if current_node == current_node.parent.left_child: 
                current_node.parent.left_child = None 
            else: current_node.parent.right_child = None 
        elif current_node.has_both_children():  
            succ = current_node.find_successor() 
            succ.splice_out() 
            current_node.key = succ.key 
            current_node.payload = succ.payload

        else:
            if current_node.has_left_child(): 
                if current_node.is_left_child(): 
                    current_node.left_child.parent = current_node.parent 
                    current_node.parent.left_child = current_node.left_child 
                elif current_node.is_right_child(): 
                    current_node.left_child.parent = current_node.parent 
                    current_node.parent.right_child = current_node.left_child 
                else: current_node.replace_node_data(current_node.left_child.key, current_node.left_child.payload, current_node.left_child.left_child, current_node.left_child.right_child) 
            else: 
                if current_node.is_left_child(): 
                    current_node.right_child.parent = current_node.parent 
                    current_node.parent.left_child = current_node.right_child 
                elif current_node.is_right_child(): 
                    current_node.right_child.parent = current_node.parent 
                    current_node.parent.right_child = current_node.right_child 
                else: current_node.replace_node_data(current_node.right_child.key, current_node.right_child.payload, current_node.right_child.left_child, current_node.right_child.right_child)

my_tree = BinaryTree(1)
my_tree.insert_left(2)
my_tree.insert_left(3)
my_tree.insert_left(4)
my_tree.insert_left(5)
my_tree.insert_left(6)
my_tree.insert_left(7)
my_tree.insert_left(8)
my_tree.insert_left(9)
print(my_tree)








