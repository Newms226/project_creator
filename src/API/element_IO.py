import abc


class ElementWriter(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, parsing_config: ParseConfig):
        pass

    @abc.abstractmethod
    def write_git_status(self, element) -> bool:
        pass

    @abc.abstractmethod
    def write_type(self, element) -> str:
        pass

    @abc.abstractmethod
    def write_name(self, element) -> str:
        pass

    @abc.abstractmethod
    def write_attributes(self, element) -> dict:
        pass


class ElementReader(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, parsing_config: ParseConfig):
        pass

    @abc.abstractmethod
    def get_git_status(self, element) -> bool:
        pass

    @abc.abstractmethod
    def get_type(self, element) -> str:
        pass

    @abc.abstractmethod
    def get_name(self, element) -> str:
        pass

    @abc.abstractmethod
    def get_attributes(self, element) -> dict:
        pass
