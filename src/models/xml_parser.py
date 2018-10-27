from models import XMLElement, FOLDER_STR, FILE_STR, IMPORT_STR, \
    get_file_separator, get_folder_separator, ParseError


class Unit(object):
    def __init__(self, name: str, element_type: str, git_track: bool,
                 suffix: str=''):
        self.git_track: bool = git_track
        self.element_type: str = element_type
        self.name: str = name
        self.suffix: str = suffix

    def __str__(self):
        return f'{self.name}{self.suffix}' if self.git_track \
            else f'{self.name}{self.suffix} (not tracked)'

    def __full_str__(self):
        return f'{self.name}: type={self.element_type}, tracked=' \
               f'{self.git_track}'

# ----------------------------------------------------------------------------+
#                                                                             |
#                                                                             |
#                              PARSING METHODS                                |
#                                                                             |
#                                                                             |
# ----------------------------------------------------------------------------+


def get_git_status(element: XMLElement) -> bool:
    directive = element.get('git')
    if not directive:
        return True
    else:
        if directive == 'True':
            return True
        else:
            return False


def get_element_type(element: XMLElement) -> str:
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


def is_folder(element: XMLElement) -> bool:
    return get_element_type(element) == FOLDER_STR


def is_file(element: XMLElement) -> bool:
    return get_element_type(element) == FILE_STR


def get_name(element: XMLElement) -> str:
    return element.tag


def get_file_extension(element: XMLElement) -> str:
    extension = element.findtext('extension')
    if not extension:
        raise ParseError(f'{element.tag} did not have a valid extension')
    return extension


def get_element_suffix(element: XMLElement,
                       folder_separator: str = get_folder_separator(),
                       file_separator: str = get_file_separator()
                       ) -> str:  # TODO Should the client be able to overwrite
    if is_folder(element):
        return folder_separator
    else:
        return file_separator + get_file_extension(element)

