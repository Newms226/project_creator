from src.parse import XMLElement, XMLParseError, ImmutableUnit, PARSING_DICT
from src import TreeNodeAPI, ReaderAPI
from warnings import warn


# noinspection PyPep8Naming
def parse_2D(xml_root: XMLElement, text_to_find: str) -> dict:
    print(f'  _xml_meta(xml_file={xml_root}, text_to_find={text_to_find}')

    to_return: dict = {}

    for element in list(xml_root.find(text_to_find)):
        if len(element) == 0:
            print(f'   {element.tag} found. len=0, text={element.text}')
            to_return[element.tag] = element.text
        else:
            print(f'   {element.tag} found. len={len(element)}')
            to_return[element.tag]: dict = {}
            for sub in list(element):
                print(f'    {sub.tag} found. text={sub.text}, len={len(sub)}')
                if len(sub) != 0:
                    warn(f'SUB CALL WHEN LEN = {len(sub)}')
                to_return[element.tag][sub.tag] = sub.text

    return to_return


class XMLReader(ReaderAPI):

    def name(self, element: XMLElement) -> str:
        return element.tag

    def git_track(self, element: XMLElement) -> bool:
        print(f'  git_track(element_name={element.tag}')
        directive = element.get(PARSING_DICT['git_attr'])
        if directive is None:
            print(f'   git_track found no directive')
            return True
        else:
            if directive == PARSING_DICT['git_track']['track']:
                print(f'   git_track found {directive} returning TRUE')
                return True
            elif directive == PARSING_DICT['git_track']['ignore']:
                print(f'   git_track found {directive} returning FALSE')
                return False

    def element_type(self, element: XMLElement) -> str:
        return element.get(PARSING_DICT['type_attr'])


XML_READER = XMLReader()


def parse_contents(element: XMLElement, reader=XML_READER,
                   require_folder=True, max_loop: int=2) -> dict:
    print(f'  parse_contents(element={element})')

    def parse(dictionary: dict, tag: str, content, count=0) -> int:
        dictionary[tag] = content
        count = count + 1
        print(f'    parse(tag={tag}, content={content}, count={count}, '
              f'dictionary={dictionary}')
        return count

    def loop(e: XMLElement, dictionary: dict, count=0):
        if count > max_loop:
            raise Exception(f'Max loop exceeded. count={count} max={max_loop}')

        if len(e) == 0:
            print(f'   len = 0')
            parse(dictionary, e.tag, e.text)
        else:
            print(f'   sub add: len = {len(e)}')
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

    print(f'  parsed={to_return}')
    return to_return


class XMLTreeNode(TreeNodeAPI, ImmutableUnit):

    def __init__(self, element: XMLElement, reader=XML_READER):
        self.element = element
        ImmutableUnit.__init__(name=reader.name(element),
                               unit_type=reader.element_type(element),
                               git_track=reader.git_track(element))

    def get_grand_ancestor(self):
        pass

    def children(self) -> list:
        return list(self.element)

    def path_to(self):
        pass

    def is_folder(self) -> bool:
        pass

    def is_file(self) -> bool:
        pass

    def is_import(self) -> bool:
        pass

