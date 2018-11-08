import abc
from API import FileTree


class ProjectContainer(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def file_tree(self) -> FileTree:
        pass

