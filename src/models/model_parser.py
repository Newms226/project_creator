import xml.etree.ElementTree as ET
import xml.etree.ElementTree.ParseError as ParseError


class Tree(object):
    """Simple class to provide access to the XML tree

    Attributes:
        xml_config (str): the absolute path to the XML config file
        tree: the ElementTree as parsed by xml.etree.ElementTree
        root: the root of the ElementTree as parsed by
            xml.etree.ElementTree.getroot()

    Shortcuts:
        info
        files
        folders
        autofiles
        git
        sync
    """

    def __init__(self, xml_config):
        """ Initialize the application & generate shortcuts to main
        components of the files

        :param xml_config: the location of the XML config file
        """

        self.xml_config = xml_config
        self.tree = ET.parse(xml_config)
        self.root = self.tree.getroot()

        try:
            self.info = self.tree.find('info')
            self.files = self.tree.find('files')
            self.folders = self.tree.find('folders')
            self.autofiles = self.tree.find('autofiles')
            self.git = self.tree.find('git')
            self.sync = self.tree.find('sync')
        except ParseError as err:
            print('Failed to parse: {0}'.format(err))
            raise err  # TODO error handling
