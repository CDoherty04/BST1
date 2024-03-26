from bst import BST


def print_menu():
    """Prints the menu options"""
    choice = input("Choose one of the following:\n"
                   "1) Add\n"
                   "2) Print\n"
                   "3) Quit\n")
    return choice


class Executive:

    def __init__(self):
        """Creates the initial Binary Search Tree"""
        self.BST = BST()

    def add(self):
        """Takes a comma separated list and adds to the BST"""
        pass

    def ordered_print(self):
        """Prints the tree in a user-specified order"""
        pass

    def run(self):
        """Runs the program through the Executive class"""
        while True:
            print_menu()
