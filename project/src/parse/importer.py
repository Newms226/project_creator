#from API import TreeNodeAPI
from __future__ import annotations
from logging_config import root_logger as log
from util.immutable_tuple import ImmutableConfig, ImmutableUnit
from src import ABCMeta, NodeMixin, RenderTree, PreOrderIter, find_node
from parse import PARSING_DICT
#from src.parse.xml import parse_contents as parse_xml


class ImportNode(ImmutableUnit, NodeMixin, object, metaclass=ABCMeta):

    def __init__(self, name, element_type, git_track, element=None,
                 parent=None):
        ImmutableUnit.__init__(name, element_type, git_track)
        self.parent = parent
        self.element = element
        log.debug(f'GENERATED: {self.__str__(detail=10)}')

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

    def _pre_detach(self, parent):
        log.warning(f'{self.name}.pre_detach <current={self.parent}, '
                    f'future={parent}>')
        pass

    def _post_detach(self, parent):
        log.warning(f'{self.name}.post_detach <current={self.parent}>')
        pass

    def _pre_attach(self, parent):
        log.info(f'{self.name}.pre_attach <current={self.parent}, '
                 f'future={parent}>')
        pass

    def _post_attach(self, parent):
        log.info(f'{self.name}.post_attach <current={self.parent}>')
        pass

    def get_child(self, child_name: str, max_level=2, filter_=None) \
            -> ImportNode:
        if filter_ is None:
            _f = lambda node: node.name == child_name
        else:
            _f = filter_

        return find_node(node=self,
                         filter_=_f,
                         maxlevel=max_level)

    def __str__(self, detail: int=0) -> str:
        """String representation with detail customization.

        0: lowest amount of info (simple name)
        1 - 5: name, type, & tracking status
        10: all info in __dict__
        """
        if detail <= 0:
            return f'{self.name}'
        if 1 <= detail <= 5:
            return f'{self.name} ({self.element_type}, tracked: ' \
                   f'{self.git_track})'
        if 5 < detail:
            return f'{self.name} ({self.element_type}, tracked: ' \
                   f'{self.git_track}):     {self.__dict__}'

    def __contains__(self, item, max_level: int=2):
        return find_node(node=self,
                         filter_= lambda node: node == item,
                         maxlevel=max_level) is not None


class FileTree(object):

    def __init__(self, root: NodeMixin):
        self.root = (root, )

    def get_root(self) -> ImportNode:
        return self.root[0]

    def get_render(self, root=None) -> RenderTree:
        if root is None:
            return RenderTree(self.get_root())
        else:
            return RenderTree(root)

    @property
    def node_count(self) -> int:
        i: int = -1
        for node in PreOrderIter(self.get_root()): i = i + 1
        return i

    def __str__(self, detail: int=0):
        _str = ''

        for pre, _, node in RenderTree(self.get_root()):
            _str += f'{pre}{node.__str__(detail=detail)}\n'

        return _str

    def __repr__(self):
        return f'FileTree <root={self.get_root()}, count={self.node_count}>'



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
