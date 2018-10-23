import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import ParseError

def get_git_tracking_bool(cur: Element) -> bool:
    directive = cur.get('git')
    if not directive:
        return True
    else:
        if directive == 'True':
            return True
        else:
            return False


class Unit:
    def __init__(self, element: Element):
        self.track: bool = get_git_tracking_bool(element)
        self.element_type = str(element.get('type'))
        self.name = element.tag


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
            self.root = root.find('project')
            # TODO ensure that all values are not null!

        except ParseError as err:
            print('Failed to parse: {0}'.format(err))
            raise err  # TODO error handling

        self.setup = {}
        self.parse_info()

    def parse_info(self):

        contributors = []
        for contributor in self.info.findall('contributors'):
            contributors.append(contributor.text)

        self.setup['contributors'] = contributors
        self.setup['name'] = self.info.findtext('name')
        self.setup['root_dir'] = self.info.findtext('rootdir')
        self.setup['license'] = self.info.findtext('license')
        self.setup['date'] = self.info.findtext('date')
