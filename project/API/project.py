import abc
from API import FileTree, BuildConfig


class ProjectContainer(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def file_tree(self) -> FileTree:
        pass

    @abc.abstractmethod
    def build_config(self) -> BuildConfig:
        pass
