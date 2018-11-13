import setup

PARSING_DICT: dict = {
    'file_type': 'file',
    'folder_type': 'folder',
    'import_type': 'import',

    'git_attr': 'git',
    'type_attr': 'type',
    'system_attr': 'system_attr',

    'import_strategy': 'import_strategy',
    'import_args': 'import_args',

    'system_dependencies': {
        'file_sep': '.',
        'folder_sep': '/'
    },

    'roots': {
        'meta': 'meta',
        'auto_generate': 'auto_generate',
        'git': 'git',
        'sync': 'sync',
        'language': 'language',
        'hierarchy': 'folder_root'
    },

    'files': {
        'text': 'text',
        'header': 'header',
        'extension': 'extension'
    },

    'git_track': {
        'track': 'True',
        'ignore': 'False'
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
from parse.xml_ import XMLElement, XML_READER as XMLReader, XMLTree, \
    parse as parse_xml


#from test_src.config import SimpleParsingConfiguration

