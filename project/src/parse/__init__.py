import setup

import xml.etree.ElementTree as XMLTree
from xml.etree.ElementTree import Element as XMLElement, ParseError as \
    XMLParseError

PARSING_DICT: dict = {
    'file_type': 'file',
    'folder_type': 'folder',
    'import_type': 'import',
    'git_attr': 'git',
    'type_attr': 'type',
    'system_attr': 'system_attr',
    'import_path': 'path',
    'import_strategy': 'import_strategy',
    'files': {
        'text': 'text',
        'header': 'header',
        'extension': 'extension'
    },
    'git_track': {
        'track': 'True',
        'ignore': 'False'
    },
    'roots': {
        'meta': 'meta',
        'auto_generate': 'auto_generate',
        'git': 'git',
        'sync': 'sync',
        'language': 'language',
        'hierarchy': 'folder_root'
    },
    'meta': {
        'name': 'name',
        'root_directory': 'root_dir',
        'date': {
            'month': 'month',
            'date': 'date',
            'year': 'year'
        },
        'license': 'license',
        'contributors': 'contributors',
        'contributor': 'contributor',
        'short_description': 'short_description',
        'long_description': 'long_description'
    },
    'git': {
        # TODO
    },
    'sync': {
        # TODO
    },
    'auto_generate': {
        # TODO
    }
}

from src.util.immutable_tuple import ImmutableConfig, ImmutableUnit
from src.API import ReaderAPI

from src.parse.importer import ImportNode
from src.parse.xml import XML_READER as XMLReader

#from test_src.config import SimpleParsingConfiguration

