import abc
from src.API import FileTreeAPI


class ProjectContainer(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def file_tree(self) -> FileTree:
        pass

