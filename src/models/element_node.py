from models import NodeBase, XMLElement, FOLDER_STR, FILE_STR, IMPORT_STR

from models.xml_parser import get_name, get_git_status, \
    get_element_type, get_element_suffix, Unit


class ElementNode(NodeBase):
    def __init__(self, name: str, element_type: str, git_track: bool,
                 suffix: str, element: XMLElement, parent: NodeBase = None):
        self.unit = Unit(name=name,
                         element_type=element_type,
                         git_track=git_track,
                         suffix=suffix)
        self.parent = parent
        self.xml_element = element

    def __str__(self):
        return self.unit.__str__()

    def __full_str__(self):
        return f'{self.unit.__full_str__()}: parent={self.parent}, ' \
               f'children={list(self.xml_element)}'

    def is_folder(self) -> bool:
        return self.unit.element_type == FOLDER_STR

    def is_file(self) -> bool:
        return self.unit.element_type == FILE_STR

    def is_import(self) -> bool:
        return self.unit.element_type == IMPORT_STR


def element_to_node(element: XMLElement, parent=None) -> ElementNode:
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
