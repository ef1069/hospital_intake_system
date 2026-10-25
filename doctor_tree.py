class DoctorNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): the name of the doctor.
        left (DoctorNode): the left child node
        right (DoctorNode): the right child node
    '''
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class DoctorTree:
    '''
    A class to represent a binary tree for managing doctor structure.
    Attributes:
        root (DoctorNode): the root node of the tree, representing the team lead.
    Methods:
        insert(): inserts a new doctor under the specified name
        preorder(): reads through the tree Root-Left-Right
        inorder(): reads through the tree Left-Root-Right
        postorder(): reads through the tree Left-Right-Root
    '''
    def __init__(self):
        self.root = None

    def insert(self, parent_name, new_doctor, side, current_node = None):
        # Case 1: empty tree
        if self.root is None:
            print("Tree is empty, cannot insert without root")
            return False

        if side not in ("left", "right"):
            print(f"Invalid side: {side}")
            return False

        # Start from root if not part of recursive call
        is_search_start = current_node is None
        if current_node is None: 
            current_node = self.root

        # Case 2: found parent node
        if current_node.name == parent_name:
            if side == "left" and current_node.left is None:
                current_node.left = DoctorNode(new_doctor)
                print(f"{new_doctor} added under {parent_name} on the left")
                return True
            elif side == "right" and current_node.right is None:
                current_node.right = DoctorNode(new_doctor)
                print(f"{new_doctor} added under {parent_name} on the right")
                return True
            else:
                print(f"{parent_name} already has a {side} subordinate")
                return False

        # Case 3: Search the subtrees
        if current_node.left:
            if self.insert(parent_name, new_doctor, side, current_node.left):
                return True

        if current_node.right:
            if self.insert(parent_name, new_doctor, side, current_node.right):
                return True

        # Case 4: Parent node not found
        if is_search_start:
            print(f"Parent node {parent_name} not found in tree")
        return False

    def preorder(self, node):
        # Base Case
        if node is None:
            return []
        result = [node.name]
        # Recursive case to append list
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result

    def inorder(self, node):
        # Base Case
        if node is None:
            return []
        result = []
        result += self.inorder(node.left)
        result.append(node.name)
        result += self.inorder(node.right)

        return result

    def postorder(self, node):
        # Base Case
        if node is None:
            return[]
        result = []
        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.name)

        return result
        

def main():
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    # Test tree root
    tree.insert("Dr. John", "Dr. Yang", "right")

    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))

main()