from logging_config import root_logger as log
from parse import PARSING_DICT, ImportNode
from util.files.contents import generate_file_text


def gen_file_name(name, extension, location=None, file_separator \
        =PARSING_DICT['system_dependencies']['file_sep']) -> str:
    log.debug(f'util.files.gen_file_name(name={name}, extension={extension}, '
              f'location={location}, file_separator={file_separator})')

    file_name = name + seperator + extension

    if location is not None:
        file_name = paths.join(location, file_name)

    log.debug(f'util.files.gen_file_name RETURNED {file_name}')
    return file_name


def write_file_text(file_node: ImportNode, location,
                    prefix_new_line: bool=True, append_to: str=''):
    log.debug(f'util.files.write_file_text(file_node={file_node}, '
              f'location={location}, prefix_new_line={prefix_new_line}, '
              f'append_to={append_to})')

    text = generate_file_text(file_node=file_node,
                              prefix_new_line=prefix_new_line,
                              append_to=append_to)
    try:
        with open(location, mode='w+') as f:  # TODO mode research
            f.write(text)
            f.close()
    except OSError as e:
        log.error(msg=str(e))
        raise e   # TODO Proper error handling

    log.debug('util.files.write_file_text RETURNED')