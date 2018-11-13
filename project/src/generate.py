from parse import FileTree, ImportNode
from util import ImmutableConfig
from logging_config import root_logger as log


def generate(config: ImmutableConfig, destination):
    def _folder_loop(node: ImportNode):
        log.debug(f'generate._folder_loop(node={node.__str__(detail=10)})')
        for child in node.children:
            _generate(child)

    def _generate(node: ImportNode):
        log.debug(f'generate._generate(node={node})')

        if node is None:
            exception_str = f'Called generate._generate() when node was NONE'
            log.error(exception_str)
            raise Exception(exception_str)

        if node.is_folder():
            _folder_gen(node)
        elif node.is_file():
            _file_gen(node)
        elif node.is_import():
            _import_gen(node)
        else:
            exception_str = f'No valid type found: {node.__str__(detail=10)}'
            log.error(exception_str)
            raise Exception(exception_str)


    def _file_gen(node: ImportNode):
        pass

    def _folder_gen(node: ImportNode):
        pass

    def _import_gen(node: ImportNode):

    log.debug(f'generate(config={config}, destination={destination})')

    _folder_loop(config.folder_hierarchy.get_root())
