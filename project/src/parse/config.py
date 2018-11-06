
class SimpleBuildConfig(tuple):
    """Immutable configuration file"""

    def __init__(self, git, sync, folder_hierarchy, metadata, language,
                 auto_generate, execution=None, security=None):
        
        self.data = (git,  # 0
                     sync,  # 1
                     folder_hierarchy,  # 2
                     metadata,  # 3
                     language,  # 4
                     auto_generate,  # 5
                     execution,   # 6
                     security)  # 7
        self.git = property(fset=self._prevent_set('git'),
                            fget=self._value(0),
                            fdel=self._prevent_delete('git'))
        self.sync = property(fset=self._prevent_set('sync'),
                             fget=self._value(1),
                             fdel=self._prevent_delete('sync'))
        self.folder_hierarchy = property(fset=self._prevent_set('folder_hierarchy'),
                                         fget=self._value(2),
                                         fdel=self._prevent_delete('folder_hierarchy'))
        self.metadata = property(fset=self._prevent_set('metadata'),
                                 fget=self._value(3),
                                 fdel=self._prevent_delete('metadata'))
        self.language = property(fset=self._prevent_set('language'),
                                 fget=self._value(4),
                                 fdel=self._prevent_delete('language'))
        self.auto_generate = property(fset=self._prevent_set('auto_generate'),
                                      fget=self._value(5),
                                      fdel=self._prevent_delete('auto_generate'))
        self.execution = property(fset=self._prevent_set('execution'),
                                  fget=self._value(6),
                                  fdel=self._prevent_delete('execution'))
        self.security = property(fset=self._prevent_set('security'),
                                  fget=self._value(7),
                                  fdel=self._prevent_delete('security'))

    def _value(self, tuple_index: int):
        return self.data[tuple_index]

    def _prevent_set(self, name):
        raise Exception(f'Cannot set {name}')

    def _prevent_delete(self, name):
        raise Exception(f'Cannot delete {name}')





class SimpleParsingConfiguration:
    def folder_type(self) -> str:
        return 'folder'

    def file_type(self) -> str:
        return 'file'

    def import_type(self) -> str:
        return 'parse'

    def type_attr(self) -> str:
        return 'type'

    def git_attr(self) -> str:
        return 'git'

    def file_text(self) -> str:
        return 'text'

    def file_header(self) -> str:
        return 'header'

    def file_extension(self) -> str:
        return 'extension'

    def system_attr(self) -> str:
        return 'system_attr'

    def import_path(self) -> str:
        return 'import_path'

    def import_strategy(self) -> str:
        return 'import_strategy'
