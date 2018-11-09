from src.API import ReaderAPI
from src.parse import XMLElement, XMLParseError, ImmutableUnit, \
    PARSING_DICT, ImportNode
from warnings import warn
from src import getLogger
from logging_config import root_logger as log


# noinspection PyMethodMayBeStatic
class XMLReader(ReaderAPI):

    def name(self, element: XMLElement) -> str:
        return element.tag

    def git_track(self, element: XMLElement) -> bool:
        log.debug(f'ENTERING (element_name={element.tag})')
        directive = element.get(PARSING_DICT['git_attr'])
        if directive is None:
            log.debug(f' found no directive')
            return True
        else:
            if directive == PARSING_DICT['git_track']['track']:
                log.debug(f' found {directive} returning TRUE')
                return True
            elif directive == PARSING_DICT['git_track']['ignore']:
                log.debug(f' found {directive} returning FALSE')
                return False

    def element_type(self, element: XMLElement) -> str:
        return element.get(PARSING_DICT['type_attr'])


XML_READER = XMLReader()


def parse_contents(element: XMLElement, reader=XML_READER,
                   require_folder=True, max_loop: int=2) -> dict:
    log.debug('ENTERING', extra={'element': element,
                                 'require_folder': require_folder,
                                 'max_loop': max_loop})

    def parse(dictionary: dict, tag: str, content, count=0) -> int:
        dictionary[tag] = content
        count = count + 1
        log.debug(f'parse(tag={tag}, content={content}, count={count}, '
                  f'dictionary={dictionary})')
        return count

    def loop(e: XMLElement, dictionary: dict, count=0):
        if count > max_loop:
            raise Exception(f'Max loop exceeded. count={count} max={max_loop}')

        if len(e) == 0:
            log.debug(f'len = 0')
            parse(dictionary, e.tag, e.text)
        else:
            log.debug(f'sub add: len = {len(e)}')
            dictionary[e.tag] = {}
            for e_sub in list(e):
                loop(e_sub, dictionary[e.tag], count=count + 1)

    def raise_if_not_folder():
        if reader.element_type(element) == PARSING_DICT['folder_type']:
            raise Exception('Called parse_contents when type was folder!'
                            f'{element}')

    if require_folder:
        raise_if_not_folder()

    to_return = {}
    for child in list(element):
        loop(child, to_return)

    log.debug(f'EXIT:{to_return}')
    return to_return


def xml_to_tree_node(element: XMLElement, reader=XML_READER, parent=None):
    node = ImportNode(name=reader.name(element),
                      element_type=reader.element_type(element),
                      git_track=reader.git_track(element))
    node.__dict__.update({'element': element, 'parent': parent})
    node.__dict__.update(parse_contents(element=element,
                                        reader=reader,
                                        require_folder=False,
                                        max_loop=1))
    return node
