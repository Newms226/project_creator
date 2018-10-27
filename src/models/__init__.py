from anytree import NodeMixin as NodeBase, RenderTree
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element as XMLElement, ParseError



def get_folder_separator() -> str:
    return '/'


def get_file_separator() -> str:
    return '.'


FOLDER_STR = 'folder'
FILE_STR = 'file'
IMPORT_STR = 'import'