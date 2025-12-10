class Treenode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self, root, threshold):
        self.root = root
        self.rotations = 0
        self.threshold = threshold

    def left_rotate(self, root):
        self.rotations += 1
        y = root.right
        temp = y.left

        y.left = root
        root.right = temp

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, root):
        self.rotations += 1
        x = root.left
        temp = x.right
        x.right = root
        root.left = temp

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def insert_value(self, val):
        if not self.root:
            self.root = Treenode(val)
        else:
            self.root = self.insert(self.root, val)

    def insert(self, root, val):
        if root is None:
            return Treenode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        root.height = 1 + max(self.get_height(root.right), self.get_height(root.left))

        balance = self.get_balance(root)

        # Left heavy tree
        if balance > self.threshold:
            if self.get_balance(root.left) < 0:
                root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right heavy tree
        if balance < -self.threshold:
            if self.get_balance(root.right) > 0:
                root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_height(self, root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def inorder_traversal(self, root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        print(root.val, end=" ")
        self.inorder_traversal(root.right)


