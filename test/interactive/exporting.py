import context

from project_creator.parse.xml_ import generate_tree
from project_creator.parse.xml_ import parse

config = parse('/Users/michael/prog/python/python3/project_creator/test/resources/test_1.xml')
tree = config.folder_hierarchy
root = tree.get_root()

from anytree.exporter import JsonExporter

exp = JsonExporter(indent=2, sort_keys=True)