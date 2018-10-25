import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import ParseError
from anytree import NodeMixin, RenderTree
from models.element_parser import get_element_name, get_git_status, \
    get_element_type, get_element_suffix


class Unit(object):
    def __init__(self, name: str, suffix: str, element_type: str,
                 git_track: bool):
        self.git_track: bool = git_track
        self.element_type: str = element_type
        self.name: str = name
        self.suffix = suffix

    def __str__(self):
        return f'{self.name}{self.suffix} (tracked: {self.git_track})'


def element_to_unit(element: Element) -> Unit:
    return Unit(name=get_element_name(element),
                element_type=get_element_name(element),
                git_track=get_git_status(element))


class ElementNode(Unit, NodeMixin):
    def __init__(self, name: str, element_type: str, git_track: bool,
                 suffix: str, parent=None):
        Unit.__init__(self,
                      name=name,
                      element_type=element_type,
                      git_track=git_track,
                      suffix=suffix)
        self.parent = parent

    def __str__(self):
        return Unit.__str__(self)


def generate_element_node(element: Element, parent=None) -> ElementNode:
    return ElementNode(name=get_element_name(element),
                       element_type=get_element_type(element),
                       git_track=get_git_status(element),
                       parent=parent,
                       suffix=get_element_suffix(element))


def generate_element_node(unit: Unit, parent=None) -> ElementNode:
    return ElementNode(name=unit.name,
                       element_type=unit.element_type,
                       git_track=unit.git_track,
                       parent=parent)


def generate_element_node(unit: Unit, parent=None) -> ElementNode:
    return ElementNode(unit, parent)


def tree_to_string(root: ElementNode) -> str:
    _str = ''

    for pre, _, node in RenderTree(root):
        _str += f'{pre}{node}\n'

    return _str