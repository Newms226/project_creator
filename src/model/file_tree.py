from src.extensions import NodeMixin, RenderTree, PreOrderIter
from src.logging_config import root_logger as log

from src.model.node import ImportNode


class FileTree(object):

    def __init__(self, root: NodeMixin):
        self._data = (root, )

    @property
    def root(self) -> ImportNode:
        return self._data[0]

    @property
    def node_count(self, count_root: bool = False) -> int:
        if count_root:
            i = 0
        else:
            i = -1

        for node in PreOrderIter(self.root): i = i + 1
        return i

    def get_render(self, root=None) -> RenderTree:
        log.debug(f'(root={root})')

        if root is None:
            return RenderTree(self.root)
        else:
            return RenderTree(root)

    def __str__(self, detail: int=0):
        _str = ''

        for pre, _, node in RenderTree(self.get_root()):
            _str += f'{pre}{node.__str__(detail=detail)}\n'

        return _str

    def __repr__(self):
        return f'FileTree <root={self.root}, count={self.node_count}>'
