# Exercise 1
def flatten_list(nested_list):
    """
    Flatten an arbitrarily nested list

    Parameters
    ----------
    nested_list : nested list of int
        List with item to be either integers or list
        Example: [2,[[3,[4]], 5]]

    Returns
    -------
    flat_list : list of int
        A flattened list with only integers
        Example: [2,3,4,5]
    """

    # initialize output
    flat_list = []
    for item in nested_list:
        # if element is list, recursively flatten and add items to output
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        # if element is int, append to output
        elif isinstance(item, int):
            flat_list.append(item)
        # if any item or subitem is not list or int, raise error
        else:
            raise TypeError("List items must be of type int or list")

    return flat_list


# Exercise 2
class Node:
    """
    Each node has an integer value, and optionally has left and right children
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise ValueError("Node value must be an int")
        self._value = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        if not isinstance(left, (Node, type(None))):
            raise ValueError("Left child must be a Node")
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        if not isinstance(right, (Node, type(None))):
            raise ValueError("Right child must be a Node")
        self._right = right


def serialize_tree(root_node):
    """
    Serializes a tree from top to bottom, left to right to a list of values

    Parameters
    ----------
    root_node : root node of a binary tree
        The tree is not ordered or balanced, it's just a binary tree
        Example:
            1
           / \
          2   3
         / \ / \
           4 2

    Returns
    -------
    serial_tree :  A list of serialized values
        Example: [1,2,3,None,4,2,None]
    """

    # check type
    if not isinstance(root_node, Node):
        raise TypeError("root_node must be a Node object")

    # initialize output
    serial_tree = []

    # initialize queue
    queue = [root_node]

    # process queue
    while len(queue) > 0:

        # process queue from left to right
        node = queue.pop(0)

        # if node is None, append to output and continue
        if not node:
            serial_tree.append(node)
            continue

        # if node is not None, append value to output
        serial_tree.append(node.value)

        # if node has children, append to queue from left to right
        if node.left or node.right:
            queue.append(node.left)
            queue.append(node.right)

    return serial_tree
