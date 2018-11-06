from API import ParseConfig
from . import ElementReader as Reader, XMLElement, XMLParseError


class XMLReader(Reader):

    def __init__(self, parsing_keywords: dict):

        pass

    def get_git_status(self, element) -> bool:
        pass

    def get_type(self, element) -> str:
        pass

    def get_name(self, element) -> str:
        pass

    def get_attributes(self, element) -> dict:
        pass
