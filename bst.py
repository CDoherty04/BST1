from binarynode import BinaryNode


class BST:

    def __init__(self):
        self._root = None

    def add(self, entry):
        new_node = BinaryNode(entry)
        if self._root is None:
            self._root = new_node

        else:
            self._rec_add(new_node, self._root)

    def _rec_add(self, new_node, cur_node):

        # Check left
        if new_node.entry < cur_node.entry:
            if cur_node is None:
                cur_node = new_node
            else:
                self._rec_add(new_node, cur_node.left)

        # Check right
        elif new_node.entry > cur_node.entry:
            if cur_node is None:
                cur_node = new_node
            else:
                self._rec_add(new_node, cur_node.right)

        else:
            raise ValueError("No duplicates allowed within a Binary Search Tree")

    def search(self, key):
        return self._rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        if cur_node.entry == key:
            return cur_node.entry
        elif cur_node.entry < key:
            self._rec_search(key, cur_node.left)
        elif cur_node.entry > key:
            self._rec_search(key, cur_node.right)
        else:
            raise KeyError("Something went wrong")
