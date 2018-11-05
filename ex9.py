#10. Write a function that takes a parse tree for a mathematical expression and calculates the derivative of the expression 
# with respect to some variable

import module_bin_tree as bt
import module_stack as s
import operator

dict_keys = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 7,
    '7': 7,
    '8': 8,
    '9': 9
}

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
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_val(dict_keys[i])
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree

def postorder(tree):
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())

def postorder_eval(tree):
    opers = {'+': operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postorder_eval(tree.get_left_child())
        res2 = postorder_eval(tree.get_right_child())
        if res1 and res2:
            return opers[tree.get_root_val()](res1, res2)
        else:
            return tree.get_root_val()

my_exp = '( 5 + x )'
my_var = input('Value of x: ')
dict_keys['x'] = int(my_var)
my_eval = build_parse_tree(my_exp)
print(postorder_eval(my_eval))
