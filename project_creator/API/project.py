import abc


class ProjectContainer(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def file_tree(self) -> FileTree:
        pass

