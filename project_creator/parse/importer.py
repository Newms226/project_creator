#from API import TreeNodeAPI
from __future__ import annotations

from project_creator.API.element_reader import ElementReader as ReaderAPI
from project_creator.API.tree_reader import TreeReader as TreeReaderAPI

from project_creator.parse import ImportNode, FileTree
from project_creator.logging_config import root_logger as log
from project_creator.util.immutable_tuple import ImmutableConfig
from project_creator.parse import PARSING_DICT
#from src.parse.xml import parse_contents as parse_xml


def to_tree_node(element, reader, parent=None,
                 parse_contents_: bool = True) -> ImportNode:
    log.debug(f'(element={element}, reader={reader}, parent={parent}, '
              f'parse_contents_={parse_contents_})')

    node = ImportNode(name=reader.name(element),
                      element_type=reader.element_type(element),
                      git_track=reader.git_track(element),
                      # element=element,
                      parent=parent)
    if parse_contents_:
        node.__dict__.update(reader.parse_contents(element=element,
                                                   require_folder=False,
                                                   max_loop=1))

    log.info(f'RETURNED {node.__str__(detail=10)}')
    return node


def generate_tree(folder_root, project_name: str, element_reader) -> FileTree:
    def folder_loop(parent: ImportNode, element):
        log.debug(f'folder_loop(parent={parent})')
        for child in element_reader.children(element):
            _generate(child, parent)

    def _generate(element, parent: ImportNode):
        log.debug(f'(element={element}, parent={parent})')
        if element is None:
            raise Exception('Cannot generate a null element')

        if element_reader.element_type(element) == PARSING_DICT['folder_type']:
            _parse_contents = False
        else:
            _parse_contents = True

        n = to_tree_node(element=element,
                         reader=element_reader,
                         parent=parent,
                         parse_contents_=_parse_contents)

        log.info(f'GENERATED: {n.__str__(detail=10)}')

        if n.is_folder():
            folder_loop(n, element)

    log.debug(f'(root={folder_root}, project_name={project_name}')

    node_root = ImportNode(name=project_name,
                           git_track=True,
                           element_type=PARSING_DICT['folder_type'])

    folder_loop(parent=node_root, element=folder_root)

    tree = FileTree(node_root)
    log.info(f'RETURNED {tree}')
    return tree


def parse(element_reader: ReaderAPI, tree_reader: TreeReaderAPI,
          config=None, parsing_config=None) -> ImmutableConfig:

    if parsing_config is None:
        parsing_config = PARSING_DICT

    log.debug(f'(element_reader={element_reader}, tree_reader={tree_reader}, '
              f'config={config}, parsing_config={parsing_config})')

    folders = generate_tree(folder_root=tree_reader.folder_root(),
                            project_name=tree_reader.meta()['name'],
                            element_reader=element_reader)

    to_return = ImmutableConfig(git=tree_reader.git(),
                                metadata=tree_reader.meta(),
                                sync=tree_reader.sync(),
                                folder_hierarchy=folders,
                                auto_generate=tree_reader.auto_generate(),
                                security=tree_reader.security(),
                                execution=tree_reader.execution())

    log.debug(f'RETURNED {to_return}')
    return to_return