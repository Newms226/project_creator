from __future__ import annotations
from src.extensions import NodeMixin, find_node

from src.logging_config import root_logger as log
from src.parse import PARSING_DICT
from src.util.immutable import read_only_properties
from src.util.sync import SyncHandler


@read_only_properties('_element_type')
class ImportNode(NodeMixin, object):

    def __init__(self, name: str, element_type, sync: SyncHandler,
                 element=None, parent: ImportNode = None,
                 contents: dict = None, meta=None):
        log.debug(f'(name={name}, element_type={element_type}, '
                  f'sync={sync}, element={element}, parent={parent}, '
                  f'contents={contents}, meta={meta})')

        self._name = name
        self._element_type = element_type
        self._sync: SyncHandler = sync
        self._meta = meta

        self.parent: ImportNode = parent
        self.element = element

        if contents is not None:
            self.__dict__.update(contents)

        log.debug(f'GENERATED {self.__str__(detail=10)}')

    @property
    def name(self):
        return self._name

    @property
    def element_type(self):
        return self._element_type

    @property
    def git_track(self):
        return self._sync.git_track

    @property
    def sync(self):
        return self._sync

    @property
    def meta(self):
        return self._meta

    def get_grand_ancestor(self):
        return self.ancestors[0]

    def is_folder(self) -> bool:
        return self.element_type == PARSING_DICT['folder_type']

    def is_file(self) -> bool:
        return self.element_type == PARSING_DICT['file_type']

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
            return f'{self.name} (type={self.element_type}, ' \
                   f'tracked={self.git_track})'
        if 5 < detail:
            return f'{self.name} (type={self.element_type}, ' \
                   f'sync: ={self.sync}, __dict__={self.__dict__})'

    def __contains__(self, item, max_level: int=2):
        return find_node(node=self,
                         filter_=lambda node: node == item,
                         maxlevel=max_level) is not None

if __name__ == '__main__':
    sync = SyncHandler(False)
    n = ImportNode('NAME', 'TYPE', sync)
    n._unit = 5
    print(n.__dict__)