from xml.etree.ElementTree import Element
from xml.etree.ElementTree import ParseError
from anytree import NodeMixin, RenderTree
from models import config


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


def is_file(element: Element) -> bool:
    return get_element_type(element) is 'file'


def get_element_name(element: Element) -> str:
    return element.tag


def get_element_extension(element: Element) -> str:
    extension = element.findtext('extension')
    if not extension:
        raise ParseError(f'{element.tag} did not have a valid extension')
    return extension


def get_element_suffix(element: Element,
                       folder_separator: str = config.get_folder_separator(),
                       file_separator: str = config.get_file_separator()
                       ) -> str:  # TODO Should the client be able to overwrite
    if is_folder(element):
        return folder_separator
    else:
        return file_separator + get_element_extension(element)

