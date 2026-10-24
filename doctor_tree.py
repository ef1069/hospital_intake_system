class DoctorNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, new_value, side, current_node = None):
        # Case 1: empty tree
        if self.root is None:
            print("Tree is empty, cannot insert without root")
            return

        # Start from root if not part of recursive call
        if current_node is None: 
            current_node = self.root

        # Case 2: found parent node
        if current_node == parent_name:
            if side == "left" and current_node.left is None:
                current_node.left = DoctorNode(new_value)
                print(f"{new_value} added under {parent_name} on the left")
                return True
            elif side == "right" and current_node.right is None:
                current_node.right = DoctorNode(new_value)
                print(f"{new_value} added under {parent_name} on the right")
                return True
            else:
                print(f"{parent_name} already has a {side} subordinate")

        # Case 3: Search the subtrees
        found_left = False
        found_right = False

        if current_node.left:
            found_left = self.insert(parent_name, new_value, side, current_node.left)

        if current_node.right and not found_left:
            found_right = self.insert(parent_name, new_value, side, current_node.right)

        # Case 4: Parent node not found
        if not (found_left or found_right):
            if current_node == self.root:
                print(f"Parent node {parent_name} not found in tree")
                return False

        return True
                 
    def preorder(self, node):
        # Base Case
        if node is None:
            return []
        
        result = [node.value]
        # Recursive case to append list
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result

    def inorder(self, node):
        # Base Case
        if node is None:
            return []
        result = []
        result+= self.preorder(node.left)
        result.append(node.value)
        result += self.preorder(node.right)

        return result

    def postorder(self, node):
        # Base Case
        if node is None:
            return[]
        result = []
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        result.append(node.value)

        return result
        

def main():
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))

main()