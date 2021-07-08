from unittest import TestCase
from BinaryTree.bintree import bin_tree_node


class TestBin_tree_node(TestCase):
    def test_make_tree(self):
        values = [3, 2, 1, 4, 5, 3]
        new_tree = bin_tree_node.make_tree(values)
        for single_value in values:
            self.assertTrue(new_tree.contains_value(single_value))
        self.assertFalse(new_tree.contains_value(7))
        self.assertTrue(new_tree.is_valid_tree())

    def test_add_value(self):
        values = [0, 1, 2, 3, 4, 5]
        root = bin_tree_node(values[0])
        for single_value in values[1:]:
            root.add_value(single_value)

    def test_contains_value(self):
        values = [3, 2, 1, 4, 5, 3]
        new_tree = bin_tree_node.make_tree(values)
        for single_value in values:
            self.assertTrue(new_tree.contains_value(single_value))
        self.assertFalse(new_tree.contains_value(7))

    def test_get_tree_as_list(self):
        values = [3, 2, 1, 4, 5, 3, 3, 3, 4, 2, 1, 2]
        new_tree = bin_tree_node.make_tree(values)
        values.sort()
        self.assertEqual(values, new_tree.get_tree_as_list())
