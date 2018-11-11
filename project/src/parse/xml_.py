from xml.etree import ElementTree as XMLTree
from xml.etree.ElementTree import Element as XMLElement, ParseError as \
    XMLParseError

from logging_config import root_logger as log, getLogger

from API import ReaderAPI
from util import ImmutableUnit
from parse import PARSING_DICT, ImportNode, FileTree
from warnings import warn


# noinspection PyMethodMayBeStatic
class XMLReader(ReaderAPI):

    def name(self, element: XMLElement) -> str:
        return element.tag

    def git_track(self, element: XMLElement) -> bool:
        log.debug(f'ENTERING git_track(element_name={element.tag})')
        directive = element.get(PARSING_DICT['git_attr'])
        if directive is None:
            log.debug(f' found no directive')
            return True
        else:
            if directive == PARSING_DICT['git_track']['track']:
                log.debug(f' found {directive} returning TRUE')
                return True
            elif directive == PARSING_DICT['git_track']['ignore']:
                log.debug(f' found {directive} returning FALSE')
                return False

    def element_type(self, element: XMLElement) -> str:
        _type = element.get(PARSING_DICT['type_attr'])
        log.debug(f' returning from element_type(tag={element.tag} with '
                  f'{_type})')
        return _type


XML_READER = XMLReader()


def parse_contents(element: XMLElement, reader=XML_READER,
                   require_folder=True, max_loop: int=2) -> dict:
    log.debug('ENTERING', extra={'element': element,
                                 'require_folder': require_folder,
                                 'max_loop': max_loop})

    def parse_dict(dictionary: dict, tag: str, content, count=0) -> int:
        dictionary[tag] = content
        count = count + 1
        log.debug(f'parse(tag={tag}, content={content}, count={count}, '
                  f'dictionary={dictionary})')
        return count

    def loop(e: XMLElement, dictionary: dict, count=0):
        if count > max_loop:
            raise Exception(f'Max loop exceeded. count={count} max={max_loop}')

        if len(e) == 0:
            log.debug(f'len = 0')
            parse_dict(dictionary, e.tag, e.text)
        else:
            log.debug(f'sub add: len = {len(e)}')
            dictionary[e.tag] = {}
            for e_sub in list(e):
                loop(e_sub, dictionary[e.tag], count=count + 1)

    def raise_if_not_folder():
        if reader.element_type(element) == PARSING_DICT['folder_type']:
            raise Exception('Called parse_contents when type was folder!'
                            f'{element}')

    if require_folder:
        raise_if_not_folder()

    to_return = {}
    for child in list(element):
        loop(child, to_return)

    log.debug(f'EXIT:{to_return}')
    return to_return


def xml_to_tree_node(element: XMLElement, reader=XML_READER, parent=None,
                     parse_contents_: bool=True):
    node = ImportNode(name=reader.name(element),
                      element_type=reader.element_type(element),
                      git_track=reader.git_track(element))
    node.__dict__.update({'element': element, 'parent': parent})
    node.parent = parent

    if parse_contents_:
        node.__dict__.update(parse_contents(element=element,
                                            reader=reader,
                                            require_folder=False,
                                            max_loop=1))

    log.info(f'GENERATED NODE: {node.__str__(detail=10)}')
    return node


def generate_tree(root: XMLElement, project_name: str) -> FileTree:

    def folder_loop(parent: ImportNode):
        log.debug(f'generate_tree.folder_loop(parent={parent})')
        for child in list(parent.element):
            _generate(child, parent)

    def _generate(element: XMLElement, parent: ImportNode):
        log.debug(f'generate_tree._generate(element={element},'
                  f'parent={parent})')
        if element is None:
            raise Exception('Cannot generate a null element')

        _parse_contents = XML_READER.element_type(element)
        if _parse_contents == PARSING_DICT['folder_type']:
            _parse_contents = False
        else:
            _parse_contents = True

        n = xml_to_tree_node(element=element, parent=parent,
                             parse_contents_=_parse_contents)
        n.element = element
        log.info(f'GENERATED: {n.__str__(detail=10)}')

        if n.is_folder():
            folder_loop(n)

    log.debug(f'generate_tree(root={root}, project_name={project_name}')

    folder_root: XMLElement = root.find(PARSING_DICT['roots']['hierarchy'])
    node_root = ImportNode(name=project_name,
                           git_track=True,
                           element_type=PARSING_DICT['folder_type'])
    node_root.element = folder_root

    folder_loop(node_root)

    tree = FileTree(node_root)
    log.info(f'GENERATED: {tree}')
    return tree


def parse(xml_file, config=None, parsing_config: dict=PARSING_DICT):
    print(f'parse.xml.parse(xml_file={xml_file}, config={config}, '
          f'parsing_config={parsing_config})')
    root = ElementTree.parse(xml_file).getroot()

    _meta = parse_contents(root, parsing_dict['roots']['meta'])
    _language = parse_contents(root, parsing_dict['roots']['language'])
    _auto_generate = parse_contents(root, parsing_dict['roots']['auto_generate'])
    _git = parse_contents(root, parsing_dict['roots']['git'])
    _sync = parse_contents(root, parsing_dict['roots']['sync'])
    _folders = generate_tree()
    _security = None
    _execution = None

    return ImmutableConfig(git=_git, metadata=_meta, language=_language,
                           sync=_sync, folder_hierarchy=_folders,
                           auto_generate=_auto_generate, security=_security,
                           execution=_execution)


if __name__ == '__main__':
    root = XMLTree.parse('/Users/michael/prog/python/python3/project_creator/project/tests/resources/basic_project.xml') \
        .getroot()
    tree = generate_tree(root, 'test')
    print(f'{tree}\n')
    print(tree.get_root().get_child('design').children)
