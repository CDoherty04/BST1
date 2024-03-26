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

        while True:
            order = input("Which order would you like to print in?\n"
                          "1) Pre Order\n"
                          "2) In Order\n"
                          "3) Post Order\n")

            print()

            # List of nodes that are taken in a certain order to be printed later
            nodes = []

            if order == "1":
                self.BST.preorder(nodes.append)
                break
            elif order == "2":
                self.BST.inorder(nodes.append)
                break
            elif order == "3":
                self.BST.postorder(nodes.append)
                break
            else:
                print("That is not a valid option, enter 1, 2, or 3.")

    def run(self):
        """Runs the program through the Executive class"""
        while True:
            choice = print_menu().lower()
            print()

            match choice:
                case "1":
                    self.add()
                case "add":
                    self.add()
                case "2":
                    self.ordered_print()
                case "print":
                    self.ordered_print()
                case "3":
                    quit()
                case "quit":
                    quit()
                case _:
                    print("That is an invalid option")
