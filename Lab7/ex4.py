class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
  
# AVL tree class which supports the  
# Insert operation 
class AVL_Tree(object): 
  
    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        # Case 3b: Left Right Case
        if balance > 1 and key > root.left.val:
            print("Case 3b: adding a node to an inside subtree")
            root.left = self._lr_rotate(root.left)
            return self.rightRotate(root)

        # Case 3b: Right Left Case
        if balance < -1 and key < root.right.val:
            print("Case 3b: adding a node to an inside subtree")
            root.right = self._rl_rotate(root.right)
            return self.leftRotate(root)
        
        # Case 3a: Adding a node to an outside subtree
        if balance > 1 and key < root.left.val:
            print("Case #3a: adding a node to an outside subtree")
            return self.rightRotate(root)

        if balance < -1 and key > root.right.val:
            print("Case #3a: adding a node to an outside subtree")
            return self.leftRotate(root)

        # Left Left Case
        if balance > 1 and key < root.left.val:
            print("Case 2: A pivot exists, and a node was added to the shorter subtree")
            return self.rightRotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.val:
            print("Case 2: A pivot exists, and a node was added to the shorter subtree")
            return self.leftRotate(root)

        if balance == 1:
            print("Case 1: Pivot not detected")
            return root
        
        
        return root
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    ########## Question 1:
    def _left_rotate(self, node):
        y = node.right
        node.right = y.left
        y.left = node
        
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y
    
    ########## Question 2:
    def _right_rotate(self, node):
        y = node.left
        node.left = y.right
        y.right = node
        
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y

    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 

    def _lr_rotate(self, node):
        y = node.left
        if y and y.right:
            x = y.right
            y.right = x.left
            x.left = y
            node.left = x
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
            return node
        else:
            return node

    def _rl_rotate(self, node):
        z = node.right
        if z and z.left:  # Check that z and z.left are not None
            T2 = z.left
            z.left = T2.right
            node.right = T2.left
            T2.right = node
            T2.left = z
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
            return node
        else:
            return node  # Return the node as is if rotation can't be performed

# Tests that test out every single case:
myTree = AVL_Tree() 
root = None
print("-----------------") 
print("Cases 1, 2, 3a, 3b:")
root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40) 
root = myTree.insert(root, 50) 
root = myTree.insert(root, 25)
root = myTree.insert(root, 35)
root = myTree.insert(root, 15)
print("-----------------")