from xml.etree.ElementTree import Element
from anytree import NodeMixin
from models.element_parser import get_name, get_git_status, \
    get_element_type, get_element_suffix, Unit


class ElementNode(NodeMixin):
    def __init__(self, name: str, element_type: str, git_track: bool,
                 suffix: str, element: Element, parent: NodeMixin = None):
        self.unit = Unit(name=name,
                         element_type=element_type,
                         git_track=git_track,
                         suffix=suffix)
        self.parent = parent
        self.xml_element = element

    def __str__(self):
        return Unit.__str__(self)

    def is_folder(self) -> bool:
        return self.unit.element_type == 'folder'  # TODO DANGEROUS!

    def is_file(self) -> bool:
        return self.unit.element_type == 'file'  # TODO DANGEROUS!

    def is_import(self) -> bool:
        return self.unit.element_type == 'import'  # TODO DANGEROUS!


def element_to_node(element: Element, parent=None) -> ElementNode:
    return ElementNode(name=get_name(element),
                       element_type=get_element_type(element),
                       git_track=get_git_status(element),
                       parent=parent,
                       suffix=get_element_suffix(element),
                       element=element)


'''def unit_to_node(unit: Unit, parent=None) -> ElementNode:
    return ElementNode(name=unit.name,
                       element_type=unit.element_type,
                       git_track=unit.git_track,
                       parent=parent)'''
