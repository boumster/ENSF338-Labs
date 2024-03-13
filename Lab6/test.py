import sys
import re

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(tokens):
    if not tokens:
        return None

    while tokens and tokens[0] == '(':
        tokens.pop(0)
    while tokens and tokens[-1] == ')':
        tokens.pop()

    if not tokens:
        return None

    if len(tokens) == 1 and tokens[0].isdigit():
        return TreeNode(int(tokens[0]))

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    min_precedence = float('inf')
    min_operator_index = -1

    parentheses_count = 0
    for i in range(len(tokens) - 1, -1, -1):
        if tokens[i] == ')':
            parentheses_count += 1
        elif tokens[i] == '(':
            parentheses_count -= 1
        elif tokens[i] in precedence and parentheses_count == 0 and precedence[tokens[i]] <= min_precedence:
            min_precedence = precedence[tokens[i]]
            min_operator_index = i

    if min_operator_index == -1:
        return TreeNode(int(tokens[0]))

    left_tokens = tokens[:min_operator_index]
    right_tokens = tokens[min_operator_index + 1:]
    operator = tokens[min_operator_index]

    left_subtree = build_tree(left_tokens)
    right_subtree = build_tree(right_tokens)

    return TreeNode(operator, left_subtree, right_subtree)

def post_order_traversal(node):
    if node is None:
        return None

    left_value = post_order_traversal(node.left)
    right_value = post_order_traversal(node.right)

    if left_value is not None and right_value is not None:
        if node.value == '+':
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
        elif node.value == '*':
            return left_value * right_value
        elif node.value == '/':
            return left_value / right_value
    else:
        return node.value

def main():
    if len(sys.argv) != 2:
        print("Usage: python ex3.py <expression>")
        sys.exit(1)

    expression = sys.argv[1]
    tokens = re.findall(r'\(|\)|\d+|[+\-*/]', expression)

    root = build_tree(tokens)
    result = post_order_traversal(root)

    print(result)

if __name__ == "__main__":
    main()
