from model.node import ImportNode
from src.util.immutable_tuple import ImmutableConfig
from src.util.folders import WorkingDirectory, TempHandler, \
    make_folder
from src.util.files.creation import write_file_text
from logging_config import root_logger as log


def generate(config: ImmutableConfig, destination):
    def _generate(node: ImportNode, ):
        log.debug(f'(node={node.name})')

        if node is None:
            exception_str = f'Called when node was NONE'
            log.error(exception_str)
            raise Exception(exception_str)

        if node.is_folder():
            _folder_gen(node)
        elif node.is_file():
            _file_gen(node)
        else:
            exception_str = f'No valid type found: {node.__str__(detail=10)}'
            log.error(exception_str)
            raise Exception(exception_str)

    def _file_gen(node: ImportNode):
        log.debug(f'(node={node})')

        write_file_text(file_node=node, location=working_dir.absolute_dir)

    def _folder_gen(node: ImportNode):
        log.debug(f'(node={node})')

        working_dir.push(node.name)
        make_folder(working_dir.absolute_dir)

        for child in node.children:
            _generate(child)

        working_dir.pop()

    log.debug(f'(config={config}, destination_dir={destination})')

    temp_handler = TempHandler(destination=destination)
    working_dir = WorkingDirectory(root=temp_handler.temp_dir)

    for child in config.folder_hierarchy.get_root().children:
        _generate(child)

    temp_handler.finalize()

    log.debug(f'RETURNED {destination}')
    return temp_handler.temp_dir


if __name__ == '__main__':
    from parse.importer import parse

    str_ = generate(
            parse('/Users/michael/Desktop/rose.xml'), 'NONE')
    print('\n' + str_)
