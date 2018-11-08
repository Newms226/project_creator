#from API import TreeNodeAPI
from util.immutable_tuple import ImmutableConfig, ImmutableUnit
from src import ABCMeta, NodeMixin
from src.parse import PARSING_DICT


class ImportNode(ImmutableUnit, metaclass=ABCMeta):

    def __init__(self, name, element_type, git_track, element=None,
                 contents=None, parent=None):
        ImmutableUnit.__init__(name, element_type, git_track)
        self.parent = parent
        self.element = element

    def get_grand_ancestor(self):
        return self.ancestors[0]

    def get_file_path(self, root=None):
        pass  # TODO

    def is_folder(self) -> bool:
        return self.element_type == PARSING_DICT['folder_type']

    def is_file(self) -> bool:
        return self.element_type == PARSING_DICT['file_type']

    def is_import(self) -> bool:
        return self.element_type == PARSING_DICT['import_type']


def from_xml(xml_file, config, parsing_config):
    print(f'STUBBED: parse.xml(xml_file={xml_file}, config={config}, '
          f'parsing_config={parsing_config})')
    root = ElementTree.parse(xml_file).getroot()

    parsing_dict = _read_parsing_config(parsing_config)
    _meta = parse_2D(root, parsing_dict['roots']['meta'])
    _language = parse_2D(root, parsing_dict['roots']['language'])
    _auto_generate = parse_2D(root, parsing_dict['roots']['auto_generate'])
    _git = parse_2D(root, parsing_dict['roots']['git'])
    _sync = parse_2D(root, parsing_dict['roots']['sync'])
    _folders = None
    _security = None
    _execution = None

    return ImmutableConfig(git=_git, metadata=_meta, language=_language,
                           sync=_sync, folder_hierarchy=_folders,
                           auto_generate=_auto_generate, security=_security,
                           execution=_execution)

"""
def from_json(json_file, config, reader: Reader) -> ConfigAPI:
    print(f'STUBBED parse.json(json_file={json_file}, config={config}, '
          f'reader={reader})')
    pass  # TODO


def from_folder(folder_root, config, metadata, reader: Reader) -> ConfigAPI:
    print(f'STUBBED parse.folder(folder_root={folder_root}, config={config}, '
          f'metadata={metadata}, reader={reader})')
    pass  # TODO


def from_project(project: ProjectContainer, config, metadata, reader: Reader) \
        -> ConfigAPI:
    print(f'STUBBED parse.project(project={project}, config={config}, '
          f'metadata={metadata}, reader={reader})')
    pass  # TODO
"""

if __name__ == '__main__':
    print(parse_2D(ElementTree.parse('/Users/michael/prog/python/python3/'
                                      'project_creator/project/tests/resources'
                                      '/basic_project.xml').getroot(),
                   _read_parsing_config(None)['roots']['meta']))
