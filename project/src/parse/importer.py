from src import BuildConfig as ConfigAPI, ProjectContainer
from src.parse import XMLElement, ElementTree, SimpleBuildConfig


def _read_parsing_config(file) -> dict:
    print(f' _read_parsing_config(file={file}) -> HARDWIRED VALUES')
    return {
        'file_type': 'file',
        'folder_type': 'folder',
        'import_type': 'parse',
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


# noinspection PyPep8Naming
def parse_2D(xml_root: XMLElement, text_to_find: str) -> dict:
    print(f'  _xml_meta(xml_file={xml_root}, text_to_find={text_to_find}')

    to_return: dict = {}

    for element in list(xml_root.find(text_to_find)):
        if len(element) == 0:
            print(f'   {element.tag} found. len=0, text={element.text}')
            to_return[element.tag] = element.text
        else:
            print(f'   {element.tag} found. len={len(element)}')
            to_return[element.tag]: dict = {}
            for sub in list(element):
                print(f'    {sub.tag} found. text={sub.text}, len={len(sub)}')
                to_return[element.tag][sub.tag] = sub.text

    return to_return


def from_xml(xml_file, config, parsing_config) -> ConfigAPI:
    print(f'STUBBED: parse.xml(xml_file={xml_file}, config={config}, '
          f'parsing_config={parsing_config})')
    root = ElementTree.parse(xml_file).getroot()

    parsing_dict = _read_parsing_config(parsing_config)
    _meta = parse_2D(root, parsing_dict['roots']['meta'])
    _language = parse_2D(root, parsing_dict['roots']['language'])
    _auto_generate = parse_2D(root, parsing_dict['roots']['auto_generate'])
    _git = parse_2D(root, parsing_dict['roots']['git'])
    _sync = parse_2D(root, parsing_dict['roots']['sync'])

    return SimpleBuildConfig(git=_git,
                             language=_language,
                             metadata=_meta,
                             auto_generate=auto_generate,
                             sync=sync,
                             )

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
