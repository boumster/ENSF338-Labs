class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.balance = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, node)
        self.update_balances(node)

    def _insert(self, current, node):
        if node.key <= current.key:
            if current.left is None:
                current.left = node
            else:
                self._insert(current.left, node)
        else:
            if current.right is None:
                current.right = node
            else:
                self._insert(current.right, node)

    def update_balances(self, node):
        while node is not None:
            node.balance = self.calculate_balance(node)
            node = self.parent(node)

    def parent(self, node):
        current = self.root
        parent = None
        while current is not node:
            parent = current
            if node.key <= current.key:
                current = current.left
            else:
                current = current.right
        return parent

    def calculate_balance(self, node):
        if node is None:
            return 0
        return self.calculate_height(node.left) - self.calculate_height(node.right)

    def calculate_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.calculate_height(node.left), self.calculate_height(node.right))
    
    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.key:
                return current
            elif data < current.key:
                current = current.left
            else:
                current = current.right
        return None

import random
import timeit

def main():
    bst = BinarySearchTree()
    for i in range(1000):
        bst.insert(random.randint(0, 1000))
    print(bst.root.balance)
    search_tasks = list(range(1000))
    random.shuffle(search_tasks)
    for task in search_tasks:
        result = bst.search(task)
        print(f"Searching for {task}... Found: {result is not None}")

if __name__ == "__main__":
    main()