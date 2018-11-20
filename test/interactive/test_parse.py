import xml.etree.ElementTree as ET

tree = ET.parse('/Users/michael/prog/python/python3/src/design'
                '/examples/hierarchy_config.xml')
tree_root = tree.getroot()
folder_root = tree_root.find('src')
src_element = folder_root.find('test_src')
