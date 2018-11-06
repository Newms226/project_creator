import abc
from API import FileTree


# noinspection PyUnresolvedReferences
class BuildConfig(object, metaclass=abc.ABCMeta):
    """Interface for the configuration of the execution of this project

    Attributes:
        git: github configuration settings
        folder_hierarchy: the projects folder/file set up
        sync: external sync settings
        execution: customization of the execution of this program
        parsing: customization of the parsing configuration of parse/exports
        security: security settings of the program
        metadata: various stats on the project, including on the language &
            user
    """

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    @property(fdel=_private('git'), fdel=_private('git'))
    def git(self):
        return self._git

    @abc.abstractmethod
    @property()
    def folder_hierarchy(self):
        pass

    @abc.abstractmethod
    def sync(self):
        pass

    @abc.abstractmethod
    def execution(self):
        pass

#    @abc.abstractmethod
#   def parsing(self) -> ParseConfig:
#        pass

    @abc.abstractmethod
    def security(self):
        pass

    @abc.abstractmethod
    def metadata(self):
        pass

    @abc.abstractmethod
    def language(self):
        pass

