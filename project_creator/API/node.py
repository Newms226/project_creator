import abc
from project_creator import PARSING_DICT


'''class TreeNode(NodeMixin, ImmutableUnit, object, metaclass=abc.ABCMeta):
    """Base node of the whole project_creator.

    Note:
        Methods of this class and all methods which inherit from it should
        be merely **convince methods.** Any attribute returned by these
        methods should be available in the instance level dictionary of the
        object.
    """
    # TODO everything else should go into the dictionary of the class!

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_grand_ancestor(self):
        pass

    @abc.abstractmethod
    def get_file_path(self, root=None):
        pass

    @abc.abstractmethod
    def is_folder(self) -> bool:
        pass

    @abc.abstractmethod
    def is_file(self) -> bool:
        pass

    @abc.abstractmethod
    def is_import(self) -> bool:
        pass
'''

class FileSystemNode(TreeNode, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def exists(self) -> bool:
        pass

    @abc.abstractmethod
    def file_attributes(self) -> dict:
        pass


class SyncedNode(FileSystemNode, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def last_synced(self):
        pass

    @abc.abstractmethod
    def remotes(self) -> list:
        pass

    @abc.abstractmethod
    def sync(self) -> bool:
        pass

    @abc.abstractmethod
    def diff_from_remotes(self) -> map:
        pass
