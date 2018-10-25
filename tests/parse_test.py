import xml.etree.ElementTree as ET
from models.file_system_tree import element_to_node
tree = ET.parse('/Users/michael/prog/python/python3/project_creator/design'
                '/examples/hierarchy_config.xml')
tree_root = tree.getroot()
folder_root = tree_root.find('project')
src_element = folder_root.find('src')
