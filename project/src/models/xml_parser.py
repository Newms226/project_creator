from models import XMLElement, ET, ParseError

# File system strings
from models import FILE_SEPARATOR, FOLDER_SEPARATOR

# Type strings
from models import FOLDER_TYPE, FILE_TYPE, IMPORT_TYPE
# Attribute Strings
from models import TYPE_ATTR, GIT_ATTR

# Folder Strings


# File Strings
from models import FILE_TEXT, FILE_HEADER, FILE_IMPORT_PATH, FILE_SUFFIX

# Git Strings
from models import GIT_IGNORE_ATTR_TEXT, GIT_TRACK_ATTR_TEXT, GIT_BRANCH, \
    GIT_REMOTE, GIT_LOG_IN, GIT_USERNAME, GIT_PASSWORD

# Set-up Strings
from models import GIT_CONFIG_ROOT, INFO_ROOT, SYNC_ROOT, FOLDER_ROOT

# Info Strings
from models import CONTRIBUTORS, PROJECT_NAME, LICENSE, DATE, ROOT_DIR


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
        return f'{self.name}{self.suffix}: type={self.element_type}, tracked=' \
               f'{self.git_track}'

# ----------------------------------------------------------------------------+
#                                                                             |
#                                                                             |
#                              PARSING METHODS                                |
#                                                                             |
#                                                                             |
# ----------------------------------------------------------------------------+


def get_git_status(element: XMLElement) -> bool:
    directive = element.get(GIT_ATTR)
    if not directive:
        return True
    else:
        if directive == GIT_TRACK_ATTR_TEXT:
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
    value = element.get(TYPE_ATTR)
    if not value:
        raise ParseError(f'No type was found for {element.tag} located at'
                         f' {element}')
    return value


def is_folder(element: XMLElement) -> bool:
    return get_element_type(element) == FOLDER_TYPE


def is_file(element: XMLElement) -> bool:
    return get_element_type(element) == FILE_TYPE


def is_import(element: XMLElement) -> bool:
    return get_element_type(element) == IMPORT_TYPE


def get_name(element: XMLElement) -> str:
    return element.tag


def get_file_extension(element: XMLElement) -> str:
    extension = element.findtext(FILE_SUFFIX)
    if not extension:
        raise ParseError(f'{element.tag} did not have a valid extension')
    return extension


def get_element_suffix(element: XMLElement,
                       folder_separator: str = FOLDER_SEPARATOR,
                       file_separator: str = FILE_SEPARATOR
                       ) -> str:  # TODO Should the client be able to overwrite
    if is_folder(element):
        return folder_separator
    else:
        return file_separator + get_file_extension(element)


class XMLTree(object):
    """Simple class to provide access to the XML tree
    """

    def __init__(self, xml_config):
        """ Initialize the application & generate shortcuts to main
        components of the files

        :param xml_config: the location of the XML config file
        """

        self.xml_config = xml_config
        self.tree = ET.parse(xml_config)
        root = self.tree.getroot()

        try:
            self.info = root.find(INFO_ROOT)
            self.git = root.find(GIT_CONFIG_ROOT)
            self.sync = root.find(SYNC_ROOT)
            self.folder_root = root.find(FOLDER_ROOT)
            # TODO ensure that all values are not null!

        except ParseError as err:
            print('Failed to parse: {0}'.format(err))
            raise err  # TODO error handling

        self.setup = {}
        self.parse_info()

    def parse_info(self):

        contributors = []
        for contributor in self.info.findall(CONTRIBUTORS):
            contributors.append(contributor.text)

        self.setup[CONTRIBUTORS] = contributors
        self.setup[PROJECT_NAME] = self.info.findtext(PROJECT_NAME)
        self.setup[ROOT_DIR] = self.info.findtext(ROOT_DIR)
        self.setup[LICENSE] = self.info.findtext(LICENSE)
        self.setup[DATE] = self.info.findtext(DATE)
