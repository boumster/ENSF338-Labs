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
import matplotlib.pyplot as plt

def generate_tasks():
    tasks = [i for i in range(1, 1001)]
    random_tasks = [random.sample(tasks, len(tasks)) for _ in range(1000)]
    return random_tasks

def measure_performance(tasks, bst):
    performance = []
    balance_values = []
    for task in tasks:
        for item in task:
            value = bst.search(item)
            if value is not None:
                balance_values.append(abs(value.balance))
                performance.append(timeit.timeit(lambda: bst.search(item), number=1))
    return performance, balance_values

def plot_data(balance_values, performance):
    plt.scatter(balance_values, performance)
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time')
    plt.title('Balance vs Search Time')
    plt.show()

if __name__ == "__main__":
    bst = BinarySearchTree()
    for i in range(1000):
        bst.insert(random.randint(0, 1000))
    tasks = generate_tasks()
    performance, balance_values = measure_performance(tasks, bst)
    plot_data(balance_values, performance)