#Modify the build_parse_tree and evaluate functions to handle boolean statements 
#(and, or, and not). Remember that “not” is a unary operator, so this will complicate your code somewhat.

import module_stack as s
import operator
import module_bin_tree as bt

def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    p_stack = s.Stack()
    e_tree = bt.BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fp_list:
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i == 'not':
            current_tree.set_root_val(not int(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_val(int(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/', 'and', 'or']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree