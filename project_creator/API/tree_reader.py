import abc


class TreeReader(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, file, parsing_config, reader):
        pass

    @abc.abstractmethod
    def meta(self) -> dict:
        pass

    @abc.abstractmethod
    def auto_generate(self) -> dict:
        pass

    @abc.abstractmethod
    def sync(self) -> dict:
        pass

    @abc.abstractmethod
    def git(self) -> dict:
        pass

    @abc.abstractmethod
    def folder_root(self):
        pass

    @abc.abstractmethod
    def security(self):
        pass

    @abc.abstractmethod
    def execution(self):
        pass
