import abc
import anytree

from API.node import TreeNode


class FileTree(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_root(self) -> TreeNode:
        """Return the root node (the project dir) of the tree

        Returns:
            TreeNode: The imported Node class as imported into **this** module
        """
        pass

    def get_render(self, root: TreeNode = None) -> anytree.RenderTree:
        if root is None:
            return anytree.RenderTree(self.get_root())
        else:
            return anytree.RenderTree(root)

        return

    def __str__(self):
        _str = ''

        for pre, _, node in self.get_render(self):
            _str += f'{pre}{node}\n'

        return _str

    def __repr__(self):
        return f'FileTree <root={self.get_root()}>'
