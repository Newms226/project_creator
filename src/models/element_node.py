from xml.etree.ElementTree import Element
from anytree import NodeMixin
from models.element_parser import get_name, get_git_status, \
    get_element_type, get_element_suffix, Unit


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


def element_to_node(element: Element, parent=None) -> ElementNode:
    return ElementNode(name=get_name(element),
                       element_type=get_element_type(element),
                       git_track=get_git_status(element),
                       parent=parent,
                       suffix=get_element_suffix(element))


def unit_to_node(unit: Unit, parent=None) -> ElementNode:
    return ElementNode(name=unit.name,
                       element_type=unit.element_type,
                       git_track=unit.git_track,
                       parent=parent)
