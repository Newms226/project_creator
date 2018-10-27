from anytree import NodeMixin as NodeBase

def get_folder_separator() -> str:
    return '/'


def get_file_separator() -> str:
    return '.'


FOLDER_STR = 'folder'
FILE_STR = 'file'
IMPORT_STR = 'import'
