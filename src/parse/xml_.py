from xml.etree import ElementTree as XMLTree
from xml.etree.ElementTree import Element as XMLElement

from src.parse.importer import generate_tree
from src.logging_config import root_logger as log

from src.API.element_reader import ElementReader as ReaderAPI
from src.API.tree_reader import TreeReader as TreeReaderAPI
from src.parse import PARSING_DICT


# noinspection PyMethodMayBeStatic
class XMLReader(ReaderAPI):

    def name(self, element: XMLElement) -> str:
        return element.tag

    def git_track(self, element: XMLElement) -> bool:
        log.debug(f'(element_tag={element.tag})')
        directive = element.get(PARSING_DICT['git_attr'])
        if directive is None:
            log.debug(f'RETURNED TRUE (directive={directive})')
            return True
        else:
            if directive == PARSING_DICT['git_track']['track']:
                log.debug(f'RETURNED TRUE (directive={directive})')
                return True
            elif directive == PARSING_DICT['git_track']['ignore']:
                log.debug(f'RETURNED FALSE (directive={directive})')
                return False

    def element_type(self, element: XMLElement) -> str:
        log.debug(f'tag={element.tag} (element={element})')
        type_ = element.get(PARSING_DICT['type_attr'])
        log.debug(f'RETURNED {type_}')
        return type_

    def parse_contents(self, element: XMLElement, require_folder=True,
                       max_loop: int = 2) -> dict:

        def parse_dict(dictionary: dict, tag: str, content, count=0) -> int:
            dictionary[tag] = content
            count = count + 1
            log.debug(f'(tag={tag}, content={content}, count={count}, '
                      f'dictionary={dictionary})')
            return count

        def loop(e: XMLElement, dictionary: dict, count=0):
            if count > max_loop:
                raise Exception(
                    f'Max loop exceeded. count={count} max={max_loop}')

            if len(e) == 0:
                log.debug(f'len = 0')
                parse_dict(dictionary, e.tag, e.text)
            else:
                log.debug(f'sub add: len = {len(e)}')
                dictionary[e.tag] = {}
                for e_sub in list(e):
                    loop(e_sub, dictionary[e.tag], count=count + 1)

        def raise_if_not_folder():
            if self.element_type(element) == PARSING_DICT['folder_type']:
                raise Exception('Called parse_contents when type was folder!'
                                f'{element}')

        log.debug(f'(element={element}, require_folder={require_folder}, '
                  f'max_loop={max_loop})')

        if require_folder:
            raise_if_not_folder()

        to_return = {}
        for child in list(element):
            loop(child, to_return)

        log.debug(f'RETURNED {to_return}')
        return to_return

    def children(self, element):
        return list(element)


XML_READER = XMLReader()


class XMLTreeReader(TreeReaderAPI):

    def __init__(self, file, reader: ReaderAPI = XML_READER):
        self.reader = reader
        self.root = XMLTree.parse(xml_file).getroot()

    def meta(self) -> dict:
        return reader.parse_contents(
            self.root.find(parsing_config['roots']['meta'])
        )

    def auto_generate(self) -> dict:
        return reader.parse_contents(
            self.root.find(parsing_config['roots']['auto_generate'])
        )

    def sync(self) -> dict:
        return reader.parse_contents(
            self.root.find(parsing_config['roots']['sync'])
        )

    def git(self) -> dict:
        return reader.parse_contents(
            self.root.find(parsing_config['roots']['git'])
        )

    def folder_root(self):
        return self.root

    def security(self):
        return None

    def execution(self):
        return None


if __name__ == '__main__':
    root = XMLTree.parse(
        '/Users/michael/prog/python/python3/src/test/resources/basic_project.xml') \
        .getroot()
    tree = generate_tree(root, 'test', element_reader=XML_READER)
    print(f'{tree}\n')
    print(tree.get_root().__dict__)
