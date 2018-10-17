import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError


class Tree(object):
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
            self.info = root.find('info')
            self.git = root.find('git')
            self.sync = root.find('sync')
            self.root = root.find('root')
            # TODO ensure that all values are not null!

        except ParseError as err:
            print('Failed to parse: {0}'.format(err))
            raise err  # TODO error handling

        self.setup = {}
        self.parse_info()

    def parse_info(self):
        self.setup['name'] = self.info.get('name').text

        contributors = []
        for contributor in self.info.get('contributors'):
            contributors.append(contributor)

        self.setup['contributors'] = contributors
        self.setup['rootdir'] = self.info.get('rootdir')
        self.setup['license'] = self.info.get('license')
        self.setup['date'] = self.info.get('date')