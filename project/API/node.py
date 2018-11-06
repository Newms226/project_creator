import abc


class TreeNode(object, metaclass=abc.ABCMeta):
    """Base node of the whole project.

    Note:
        Methods of this class and all methods which inherit from it should
        be merely **convince methods.** Any attribute returned by these
        methods should be available in the instance level dictionary of the
        object.
    """
    # TODO everything else should go into the dictionary of the class!

    @abc.abstractmethod
    def get_grand_ancestor(self):
        pass

    @abc.abstractmethod
    def children(self) -> list:
        pass

    @abc.abstractmethod
    def path_to(self):
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

    @abc.abstractmethod
    def git_track(self) -> bool:
        pass

    @abc.abstractmethod
    def name(self) -> str:
        pass

    @abc.abstractmethod
    def element_type(self):
        pass


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
