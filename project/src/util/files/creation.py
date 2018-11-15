from logging_config import root_logger as log
from parse import PARSING_DICT, ImportNode
from util.files.contents import generate_file_text
from os import path


def gen_file_name(name, extension, location=None,
                  file_separator=
                    PARSING_DICT['system_dependencies']['file_sep']) -> str:
    log.debug(f'(name={name}, extension={extension}, location={location}, '
              f'file_separator={file_separator})')

    file_name = _get_valid_name(name) + file_separator + extension

    if location is not None:
        file_name = path.join(location, file_name)

    log.debug(f'RETURNED {file_name}')
    return file_name


def _get_valid_name(name: str) -> str:
    log.debug(f'(name={name})')

    to_return = name.replace(' ', '_').lower()

    if to_return[0].isdigit():
        to_return = '_' + to_return

    log.debug(f'RETURNED {to_return}')
    return to_return


def write_file_text(file_node: ImportNode, location,
                    prefix_new_line: bool=True, append_to: str=''):
    log.debug(f'(file_node={file_node}, location={location}, '
              f'prefix_new_line={prefix_new_line}, append_to={append_to})')

    text = generate_file_text(file_node=file_node,
                              prefix_new_line=prefix_new_line,
                              append_to=append_to)
    path_ = gen_file_name(name=file_node.name,
                          extension=getattr(file_node, 'extension',
                                            PARSING_DICT['files']
                                                        ['default_extension']),
                          location=location)
    try:
        with open(path_, mode='w+') as f:  # TODO mode research
            f.write(text)
            f.close()
    except OSError as e:
        log.error(msg=str(e))
        raise e   # TODO Proper error handling

    log.debug(f'RETURNED {path_}')
    return path_
