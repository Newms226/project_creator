import abc


class ParseConfig(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def folder_type(self) -> str:
        pass

    @abc.abstractmethod
    def file_type(self) -> str:
        pass

    @abc.abstractmethod
    def import_type(self) -> str:
        pass

    @abc.abstractmethod
    def type_attr(self) -> str:
        pass

    @abc.abstractmethod
    def git_attr(self) -> str:
        pass

    @abc.abstractmethod
    def file_text(self) -> str:
        pass

    @abc.abstractmethod
    def file_header(self) -> str:
        pass

    @abc.abstractmethod
    def file_extension(self) -> str:
        pass

    @abc.abstractmethod
    def system_attr(self) -> str:
        pass

    @abc.abstractmethod
    def import_path(self) -> str:
        pass

    @abc.abstractmethod
    def import_strategy(self) -> str:
        pass
