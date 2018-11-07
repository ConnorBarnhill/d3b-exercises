import unittest
from coding import flatten_list, Node, serialize_tree


class TestExercise1(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(flatten_list([2, [[3, [4]], 5]]), [2, 3, 4, 5])

    def test_case_2(self):
        self.assertEqual(flatten_list([1, [2, 3]]), [1, 2, 3])

    def test_case_3(self):
        self.assertEqual(flatten_list([1, [2, 3], [4, [5, 6, [7, 8, 9]]]]),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9])


class TestExercise2(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(ValueError):
            root = Node('a')

        with self.assertRaises(ValueError):
            root = Node(1, 1)

        with self.assertRaises(ValueError):
            root = Node(1, Node(1), 1)

        root = Node(1)
        with self.assertRaises(ValueError):
            root.left = 1
        with self.assertRaises(ValueError):
            root.right = 1

    def test_case_2(self):
        root = Node(1)

        self.assertEqual(serialize_tree(root), [1])

    def test_case_3(self):
        root = Node(1)
        root.right = Node(3)

        self.assertEqual(serialize_tree(root), [1, None, 3])

    def test_case_4(self):
        root = Node(1)
        root.left = Node(2)
        root.left.right = Node(4)
        root.right = Node(3)
        root.right.left = Node(2)

        self.assertEqual(serialize_tree(root), [1, 2, 3, None, 4, 2, None])


if __name__ == '__main__':
    unittest.main()
