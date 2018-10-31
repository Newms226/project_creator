# Imported library classes & functions
# noinspection PyUnresolvedReferences
from anytree import NodeMixin as NodeBase, RenderTree
# noinspection PyUnresolvedReferences
import xml.etree.ElementTree as ET
# noinspection PyUnresolvedReferences
from xml.etree.ElementTree import Element as XMLElement, ParseError


# File system strings
from .config import FILE_SEPARATOR, FOLDER_SEPARATOR

# Type strings
from .config import FOLDER_TYPE, FILE_TYPE, IMPORT_TYPE

# Attribute Strings
from .config import TYPE_ATTR, GIT_ATTR

# Folder Strings


# File Strings
from .config import FILE_TEXT, FILE_HEADER, FILE_IMPORT_PATH, FILE_SUFFIX

# Git Strings
from .config import GIT_IGNORE_ATTR_TEXT, GIT_TRACK_ATTR_TEXT, GIT_BRANCH, \
    GIT_REMOTE, GIT_LOG_IN, GIT_USERNAME, GIT_PASSWORD

# Set-up Strings
from .config import GIT_CONFIG_ROOT, INFO_ROOT, SYNC_ROOT, FOLDER_ROOT

# Info Strings
from .config import CONTRIBUTORS, PROJECT_NAME, LICENSE, DATE, ROOT_DIR

# Imported classes / functions
from .xml_parser import XMLTree
from .tree import Tree, generate_tree
from .tree import ElementNode, FileNode, FolderNode, ImportNode


