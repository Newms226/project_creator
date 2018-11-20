import abc
from abc import ABCMeta, ABC

from parse import ImportNode


class ElementReader(ABC, object):

    @abc.abstractmethod
    def name(self, element) -> str:
        pass

    @abc.abstractmethod
    def element_type(self, element) -> str:
        pass

    @abc.abstractmethod
    def git_track(self, element) -> dict:
        pass

    @abc.abstractmethod
    def parse_contents(self, element) -> dict:
        pass

    @abc.abstractmethod
    def children(self, element) -> list:
        pass


class FileReader(ElementReader, ABC):

    @abc.abstractmethod
    def extension(self):
        pass

    @abc.abstractmethod
    def header(self):
        pass

    @abc.abstractmethod
    def text(self):
        pass

