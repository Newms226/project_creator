import abc
import anytree


class FileTree(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_root(self):
        """Return the root node (the project dir) of the tree

        Returns:
            TreeNode: The imported Node class as imported into **this** module
        """
        pass


