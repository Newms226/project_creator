from . import BuildConfig, ParseConfig


class SimpleParsingConfiguration(ParseConfig):
    def folder_type(self) -> str:
        return 'folder'

    def file_type(self) -> str:
        return 'file'

    def import_type(self) -> str:
        return 'import'

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
