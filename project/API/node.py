import abc


class Node(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_grand_ancestor(self):
        pass

    @abc.abstractmethod
    def children(self):
        pass

    @abc.abstractmethod
    def path_to(self):
        pass

    @abc.abstractmethod
    def is_folder(self):
        pass

    @abc.abstractmethod
    def is_file(self):
        pass

    @abc.abstractmethod
    def system_attr(self):
        pass

    @abc.abstractmethod
    def exists(self):
        pass
