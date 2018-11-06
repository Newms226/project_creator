import abc


class Parser(object, metaclass=abc.ABCMeta):

    __element_type__: type = None

    @abc.abstractmethod
    def __init__(self, element_type: type):
        __element_type__ = element_type

    @abc.abstractmethod
    def get_git_status(self, element: __element_type__) -> bool:
        pass

    @abc.abstractmethod
    def get_type(self, element: __element_type__) -> str:
        pass

    @abc.abstractmethod
    def get_name(self, element: __element_type__) -> str:
        pass

    @abc.abstractmethod
    def get_file_extension(self, element: __element_type__) -> str:
        pass

    @abc.abstractmethod
    def get_attributes(self, element: __element_type__) -> dict:
        pass