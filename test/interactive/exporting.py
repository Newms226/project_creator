import context

from parse.importer import generate_tree, parse

config = parse('/Users/michael/prog/python/python3/src/test/resources/test_1.xml')
tree = config.folder_hierarchy
root = tree.get_root()

from anytree.exporter import JsonExporter

exp = JsonExporter(indent=2, sort_keys=True)