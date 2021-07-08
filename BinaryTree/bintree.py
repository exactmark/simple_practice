class bin_tree_node(object):
    def __init__(self, held_value, parent=None, left=None, right=None):
        self.held_value = held_value
        self.parent = parent
        self.left = left
        self.right = right

    @staticmethod
    def make_tree(value_list):
        root = bin_tree_node(value_list[0])
        for single_value in value_list[1:]:
            root.add_value(single_value)
        return root

    def add_value(self, new_value):
        if new_value < self.held_value:
            if not self.left:
                self.left = bin_tree_node(new_value, self)
            else:
                self.left.add_value(new_value)
        else:
            if not self.right:
                self.right = bin_tree_node(new_value, self)
            else:
                self.right.add_value(new_value)

    def contains_value(self, target):
        if self.held_value == target:
            return True
        elif self.held_value > target and self.left:
            return self.left.contains_value(target)
        elif self.held_value < target and self.right:
            return self.right.contains_value(target)
        return False

    def is_valid_tree(self):
        if self.left:
            if self.left.held_value > self.held_value:
                return False
            elif not self.left.is_valid_tree():
                return False
        if self.right:
            if self.right.held_value < self.held_value:
                return False
            elif not self.right.is_valid_tree():
                return False
        return True

    def get_tree_as_list(self):
        partial_list = [self.held_value]
        if self.left:
            partial_list = self.left.get_tree_as_list() + partial_list
        if self.right:
            partial_list = partial_list + self.right.get_tree_as_list()
        return partial_list
