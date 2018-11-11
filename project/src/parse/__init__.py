import setup

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
    },
    'language': {
        # TODO
    }
}

from parse.importer import ImportNode, FileTree
from parse.xml_ import XMLElement, XML_READER as XMLReader, XMLTree


#from test_src.config import SimpleParsingConfiguration

