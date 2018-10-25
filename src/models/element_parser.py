from xml.etree.ElementTree import Element
from xml.etree.ElementTree import ParseError
from anytree import NodeMixin, RenderTree
from models import config


class Unit(object):
    def __init__(self, name: str, extension: str, element_type: str,
                 git_track: bool):
        self.git_track: bool = git_track
        self.element_type: str = element_type
        self.name: str = name
        self.extension = extension

    def __str__(self):
        return f'{self.name}{self.extension} (tracked: {self.git_track})'


def element_to_unit(element: Element) -> Unit:
    return Unit(name=get_element_name(element),
                element_type=get_element_name(element),
                git_track=get_git_status(element))


class ElementNode(Unit, NodeMixin):
    def __init__(self, name: str, element_type: str, git_track: bool,
                 parent=None):
        Unit.__init__(self,
                      name=name,
                      element_type=element_type,
                      git_track=git_track)
        self.parent = parent

    def __str__(self):
        return Unit.__str__(self)


def generate_element_node(element: Element, parent=None) -> ElementNode:
    return ElementNode(name=get_element_name(element),
                       element_type=get_element_type(element),
                       git_track=get_git_status(element),
                       parent=parent)


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


def get_git_status(element: Element) -> bool:
    directive = element.get('git')
    if not directive:
        return True
    else:
        if directive == 'True':
            return True
        else:
            return False


def get_element_type(element: Element) -> str:
    """Returns the element type

    :param element: the element to examine
    :return str: the element type as a string
    :raises ParseError: if the element was invalid / method could not find
                        the 'type' attribute
    """
    value = element.get('type')
    if not value:
        raise ParseError(f'No type was found for {element.tag} located at'
                         f' {element}')
    return value


def is_folder(element: Element) -> bool:
    return get_element_type(element) is 'folder'


def get_element_name(element: Element) -> str:
    return element.tag


def get_element_extension(element: Element) -> str:
    extension = element.findtext('extension')
    if not extension:
        raise ParseError(f'{element.tag} did not have a valid extension')
    return extension


def get_element_suffix(element: Element, element_type: str = None,
                       folder_separator: str = config.get_folder_separator(),
                       file_separator: str = config.get_file_separator()
                       ) -> str:
    if not element_type:
        t = get_element_type(element)
    else:
        t = element_type

    if is_folder(element):
        return folder_separator
    else:
        return file_separator + get_element_extension(element)

