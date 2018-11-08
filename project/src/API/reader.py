import abc


class Reader(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def name(self, element) -> str:
        pass

    @abc.abstractmethod
    def git_track(self, element) -> bool:
        pass

    @abc.abstractmethod
    def element_type(self, element) -> str:
        pass
