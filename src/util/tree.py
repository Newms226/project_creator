from anytree import RenderTree, NodeMixin
from models.element_node import ElementNode


def tree_to_string(root: ElementNode) -> str:
    _str = ''

    for pre, _, node in RenderTree(root):
        _str += f'{pre}{node}\n'

    return _str


class Tree(object):

    def __init__(self, root_node: NodeMixin): self.root = root_node

    def get_root(self) -> NodeMixin: return self.root

    def get_rendered_tree(self): return RenderTree(self.root)

    def __str__(self): return tree_to_string(self.root)

