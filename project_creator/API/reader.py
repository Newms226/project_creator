import abc
from abc import ABCMeta, ABC


class Reader(ABC, object):

    @abc.abstractmethod
    def name(self, element) -> str:
        pass

    @abc.abstractmethod
    def element_type(self, element) -> str:
        pass

    @abc.abstractmethod
    def meta(self, element) -> dict:
        pass


class FileReader(Reader, ABC):

    @abc.abstractmethod
    def extension(self):
        pass

    @abc.abstractmethod
    def header(self):
        pass

    @abc.abstractmethod
    def text(self):
        pass

