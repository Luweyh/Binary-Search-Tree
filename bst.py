# Course: CS261 - Data Structures
# Student Name: Luwey Hon
# Assignment: BST
# Description: This program implement a binary search tree
# # and adds certain feature to the binary search tree for use.
# # it has various ADT such as remove or add and defines
# # different properties for the bst such as seeing
# # if it is complete or perfect.


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        if cur.left:
            self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        if cur.right:
            self._str_helper(cur.right, values)

    def add(self, value: object) -> None:
        """
        Adds a new value to the tree
        """

        q = Queue()
        q.enqueue(value)        # add the node to the queue

        node = TreeNode(value)
        current = self.root
        flag = 0

        # when there's no node in tree, make the new node the root
        if current is None:
            current = node
            self.root = current
            flag = 1                # flag to stop next while loop

        while current is not None and flag == 0:

            # moving right in the tree
            if value >= current.value:
                if current.right is None:       # when the node position is found
                    current.right = node
                    current = None
                else:                           # when the node position is not found yet
                    current = current.right

            # moving left in the tree
            else:
                if current.left is None:        # when the node position is found
                    current.left = node
                    current = None
                else:                           # when the node position is not found yet
                    current = current.left


    def contains(self, value: object) -> bool:
        """
        Sees if the tree contains a value
        """

        # empty tree
        if self.root is None:
            return False

        current = self.root

        if current == value:
            return True

        while current is not None:
            if current.value == value:      # when the node is found
                return True
            if value < current.value:       # move to left node
                current = current.left
            else:                           # move to right node
                current = current.right

        return False

    def get_first(self) -> object:
        """
        returns the root node
        """

        if self.root is not None:
            return self.root.value

        return None

    def remove_first(self) -> bool:
        """
        Removes the root node
        """

        return self.remove(self.get_first())

    def remove(self, value) -> bool:
        """
        removes the first instance of the value found in the tree
        """

        # cant remove if the tree does not contain the value
        if self.contains(value) is False:
            return False

        previous = self.root        # the previous node before the removal
        current = self.root

        # removing the first node
        if current.value == value or current == value:
            right_node = self.root.right
            left_node = self.root.left
            left_most_node = right_node

            # when there's only the root node
            if left_node is None and right_node is None:
                self.root = None

            # when there's only 3 consective  right nodes in order
            elif left_node is None and right_node is not None and right_node.right is not None and right_node.left is None:
                self.root.right = right_node.right
                self.root = right_node

            # when there is a right child with a left child followed
            elif left_node is None and right_node is not None and right_node.left is not None:
                self.root = right_node.left
                self.root.right = right_node
                self.root.right.left = None


            # when there is only a left node
            elif left_node is not None and right_node is None:
                self.root.left = left_node.left
                self.root = left_node

            # when there is both nodes
            else:
                # finds the left most child
                while left_most_node.left is not None:
                    right_node = left_most_node
                    left_most_node = left_most_node.left

                old_right = self.root.right
                old_left = self.root.left

                # replaces left most child pointers
                if old_right.left is not None:
                    right_node.left = left_most_node.right
                    left_most_node.left = self.root.left
                    left_most_node.right = self.root.right
                    self.root = left_most_node

                # when the right node only has another right sub node
                elif old_right.right is not None and old_left is None:
                    old_right = self.root.right.right
                    self.root = self.root.right
                    self.root.left = old_left

                # when there's both nodes and right node has no child
                else:
                    old_right.left = self.root.left
                    self.root = self.root.right

            return True

        # This is removing when it's not the tree node

        # finding the right node
        while current.value != value:
            if value < previous.value:
                previous = current
                current = current.left
            else:
                previous = current
                current = current.right

        # left / right flag represent which direction to remove later
        left_flag = 0
        right_flag = 0

        if previous.right == current:
            right_flag = 1
        else:
            left_flag = 1

        # removing a leaf node which means no left or right node
        if current.right is None and current.left is None:
            if left_flag == 1:
                previous.left = None
            else:
                previous.right = None

        # when only the left node is present
        elif current.left is not None and current.right is None:
            if left_flag == 1:
                previous.left = current.left
            else:
                previous.right = current.left

        # when only the right node is present
        elif current.left is None and current.right is not None:
            if left_flag == 1:
                previous.left = current.right
            else:
                previous.right = current.right

        # when both nodes are present
        else:
            prev_left = current
            left_node = current.right       # positioning to the right node

            # getting the right's node left most child
            while left_node.left is not None:
                prev_left = left_node
                left_node = left_node.left

            if left_flag == 1:
                previous.left = left_node
            else:
                # removing the pointer on the right node's left most child
                prev_left.left = left_node.right

                # # replacing the pointers at the removal position
                previous.right = left_node
                left_node.left = current.left
                left_node.right = current.right

        return True

    def pre_order_traversal(self) -> Queue:
        """
        Finds the pre order traversal of the bst
        """
        q = Queue()
        self.pre_order_helper(self.root, q)

        return q

    def pre_order_helper(self, curr, q):
        """
        Uses recursion to find the pre-order
        """

        # base case
        if curr is None:
            return

        q.enqueue(curr.value)                       # enqueues the value

        if curr.left:                                # goes left in the tree
            self.pre_order_helper(curr.left, q)

        if curr.right:                              # goes right in the tree
            self.pre_order_helper(curr.right, q)


    def in_order_traversal(self) -> Queue:
        """
        Finds the in order traversal of the bst
        """

        q = Queue()
        self.in_order_helper(self.root, q)
        return q

    def in_order_helper(self, curr, q):
        """
        Uses recursion to find the nodes in order
        """

        # base case
        if curr is None:
            return

        if curr.left:                                   # goes left in the tree
            self.in_order_helper(curr.left, q)

        q.enqueue(curr.value)                           # enqueues the value

        if curr.right:                                  # goes right in the tree
            self.in_order_helper(curr.right, q)

    def post_order_traversal(self) -> Queue:
        """
        Finds the post order traversal for the bst
        """
        q = Queue()
        self.post_order_helper(self.root, q)
        return q

    def post_order_helper(self, curr, q):
        """
        Uses recursion to find the post order
        """

        if curr is None:                                # base case
            return

        if curr.left:                                   # go left
            self.post_order_helper(curr.left, q)

        if curr.right:                                  # go right
            self.post_order_helper(curr.right, q)

        q.enqueue(curr.value)                           # get the value


    def by_level_traversal(self) -> Queue:
        """
        Finds the by level traversal for the bst
        """
        q = Queue()
        self.by_level_helper(q, self.root)

        return q

    def by_level_helper(self, q, curr):
        """ Helper to iterate through all the level """
        for i in range(1, self.height() + 2):
            self.by_level_helper_2(q, curr, i)

    def by_level_helper_2(self, q, curr, level):
        """ Looks at the current level and enqueues the value"""

        if curr is None:        # base case
            return
        if level == 1:          # enqueues the value at the level
            q.enqueue(curr.value)

        # changes the left and right level
        elif level > 1:
            self.by_level_helper_2(q, curr.left, level-1)
            self.by_level_helper_2(q, curr.right, level - 1)

    def is_full(self) -> bool:
        """
        Check to see if the binary search tree is full
        """

        return self.is_full_helper(self.root)

    def is_full_helper(self, curr):
        """
        Helper function to see if the bst is full
        """

        # for empty tree
        if curr is None:
            return True

        # for leaf nodes
        if curr.left is None and curr.right is None:
            return True

        # when left and right are filled and its subtree is filled
        if curr.left is not None and curr.right is not None:
            return self.is_full_helper(curr.left) and self.is_full_helper(curr.right)

        return False

    def is_complete(self) -> bool:
        """
        Sees if the binary search tree is complete
        """

        # one or empty tree is considered complete
        if self.size() == 0 or self.size() == 1:
            return True

        count = 0
        size = self.size()

        return self.is_complete_helper(self.root, count, size)


    def is_complete_helper(self, curr, count, size):
        """
        Helps see if the binary search tree is complete
        """

        # base case
        if curr is None:
            return True

        # when the count of current node is more than the size, it is false
        if count >= size:
            return False

        # finding the nodes in the tree by recursion
        return ((self.is_complete_helper(curr.left, 2* count + 1, size))
            and (self.is_complete_helper(curr.right, 2 * count + 2, size )))

    def is_perfect(self) -> bool:
        """
        Sees if the binary search tree is perfect
        """

        h = self.height()

        # empty tree or one node tree is considered perfect
        if self.size() == 0 or self.size() == 1:
            return True

        # formula for perfect tree:
            # 1) It has 2^h leaves
            # 2) It ha 2^(h+1) total nodes
        if self.count_leaves() == 2**h and self.size() == 2**(h+1) - 1:     # using the formula
            return True

        return False

    def size(self):
        """
        Get the size of the bst
        """

        return self.size_helper(self.root)


    def size_helper(self, curr) -> int:
        """
        Helps find the size
        """

        if curr is None:        # empty tree
            return 0

        # finds how many nodes in the bst
        else:
            return(self.size_helper(curr.left) + 1 + self.size_helper(curr.right))


    def height(self) -> int:
        """
        Finds the height of the bst
        """

        return self.height_helper(self.root)

    def height_helper(self, curr):
        """
        Helps find the height of the bst
        """

        # empty tree
        if curr is None:
            return -1

        # find the height of the right and left side
        else:
            left_side = self.height_helper(curr.left)
            right_side = self.height_helper(curr.right)

        # finds which side has the longest height and return it
        if left_side > right_side:
            return left_side + 1
        else:
            return right_side + 1

    def count_leaves(self) -> int:
        """
        counts the leaves in the bst
        """

        return self.count_leaves_helper(self.root)

    def count_leaves_helper(self, curr):
        """
        Helps count the leaves
        """

        # when it's an empty tree
        if curr is None:
            return 0

        # when the leaf is found
        if curr.left is None and curr.right is None:
            return 1

        # recursion to get to the leaf nodes
        else:
            return self.count_leaves_helper(curr.left) + self.count_leaves_helper(curr.right)


    def count_unique(self) -> int:
        """
        Counts the number of unique nodes
        """

        queue_data = self.in_order_traversal()      # to get a Queue and all the node values
        node_vals = [None] * self.size()            # None filling the array
        count = 0

        for num in range(self.size()):
            node = queue_data.dequeue()     # looks at the dequeu value

            # increase count if the value has not been visited yet
            if node not in node_vals:
                count += 1

            # keep track of all the node values
            node_vals[num] = node

        return count



# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    # # print("\nPDF - method add() example 1")
    # print("----------------------------")
    # tree = BST()
    # print(tree)
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree)
    # tree.add(15)
    # tree.add(15)
    # print(tree)
    # tree.add(5)
    # print(tree)

    # """ add() example 2 """
    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # tree = BST()
    # tree.add(10)
    # tree.add(10)
    # print(tree)
    # tree.add(-1)
    # print(tree)
    # tree.add(5)
    # print(tree)
    # tree.add(-1)
    # print(tree)

    # """ contains() example 1 """
    # print("\nPDF - method contains() example 1")
    # print("---------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.contains(15))
    # print(tree.contains(-10))
    # print(tree.contains(15))

    # """ contains() example 2 """
    # print("\nPDF - method contains() example 2")
    # print("---------------------------------")
    # tree = BST()
    # print(tree.contains(0))

    # """ get_first() example 1 """
    # print("\nPDF - method get_first() example 1")
    # print("----------------------------------")
    # tree = BST()
    # print(tree.get_first())
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree.get_first())
    # print(tree)
    #
    # """ remove() example 1 """
    # print("\nPDF - method remove() example 1")
    # print("-------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.remove(7))
    # print(tree.remove(15))
    # print(tree.remove(15))
    # #
    # """ remove() example 2 """
    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.remove(20))
    # print(tree)
    #
    # """ remove() example 3 """
    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    # print(tree.remove(20))
    # print(tree)
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.remove(10))
    # print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    # """ remove_first() example 1 """
    # print("\nPDF - method remove_first() example 1")
    # print("-------------------------------------")
    # tree = BST([10, 15, 5])
    # print(tree.remove_first())
    # print(tree)
    # #
    # """ remove_first() example 2 """
    # print("\nPDF - method remove_first() example 2")
    # print("-------------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7])
    # # tree = BST([10, 20, 5, 7])
    # print(tree.remove_first())
    # print(tree)

    # """ remove_first() example 3 """
    # print("\nPDF - method remove_first() example 3")
    # print("-------------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # tree = BST([10, 12, 10, -1, 5, -1])
    # tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    # tree = BST([10, 5, 15])
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)


    # """ Traversal methods example 1 """
    # print("\nPDF - traversal methods example 1")
    # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())
    #
    # """ Traversal methods example 2 """
    # print("\nPDF - traversal methods example 2")
    # print("---------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())
    #
    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    # """ Comprehensive example 2 """
    # print("\nComprehensive example 2")
    # print("-----------------------")
    # tree = BST()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'N/A   {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')
    #
    # for value in 'DATA STRUCTURES':
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print('', tree.pre_order_traversal(), tree.in_order_traversal(),
    #       tree.post_order_traversal(), tree.by_level_traversal(),
    #       sep='\n')

