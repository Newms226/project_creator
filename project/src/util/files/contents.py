from logging_config import root_logger as log
from parse import ImportNode, PARSING_DICT
from util.strings import require_string
from warnings import warn


def _prefix_handler(append_to: str,
                    generated_text: str,
                    prefix_new_line: bool = True,
                    new_line_char: str = '\n') -> str:
    log.debug(f'util.files._prefix_handler(append_to={append_to}, '
              f'generated_text={generated_text}, '
              f'prefix_new_line={prefix_new_line}, '
              f'new_line_char={new_line_char})')

    if prefix_new_line:
        to_return = append_to + new_line_char + generated_text
    else:
        to_return = append_to + generated_text

    log.debug(f'util.files._prefix_handler RETURNED {to_return}')
    return to_return


def append_header(header_contents: str, append_to: str= '', rst_header=True,
                  rst_char: str = '=', prefix_new_line=True,
                  overline: bool=False) -> str:
    log.debug(f'util.files.append_header(header_contents={header_contents},'
              f'append_to={append_to}, rst_header={rst_header}, '
              f'rst_char={rst_char}, prefix_new_line={prefix_new_line}, '
              f'overline={overline})')

    if not rst_header:
        log.info('rst_header was false, simple appending...')

        header_text = _prefix_handler(append_to=append_to,
                                      generated_text=header_contents,
                                      prefix_new_line=prefix_new_line)

        log.debug(f'util.files.append_header RETURNED {header_text}')
        return header_text

    header_underline = _generate_header_underline(header=header_contents,
                                                  header_char=rst_char)
    header_text = header_contents + '\n' + header_underline
    if overline:
        header_text = header_underline + '\n' + header_text

    header_text = _prefix_handler(append_to=append_to,
                                  generated_text=header_text,
                                  prefix_new_line=prefix_new_line)

    log.debug(f'util.files.append_header RETURNED {header_text}')
    return header_text


def _generate_header_underline(header, header_char: str = '=') -> str:
    log.debug(f'util.files._generate_header(header_char={header_char})')

    if len(header_char) != 1:
        raise Exception('header_char MUST be a char (len == 1)')

    delimiter_text = header_char + (header_char * len(header))

    log.debug(f'util.files._generate_header RETURNED {delimiter_text}')
    return delimiter_text


def append_text(text, append_to: str='', prefix_new_line: bool = True) -> str:
    log.debug(f'util.files.append_text(text={text}, append_to={append_to},'
              f'prefix_new_line={prefix_new_line}')

    text = _prefix_handler(append_to=append_to,
                           generated_text=text,
                           prefix_new_line=prefix_new_line)

    log.debug(f'util.files.append_text RETURNED {text}')
    return text


def append_import(strategy, args, append_to: str = None,
                  suffix_new_line: bool = None) -> str:
    log.debug(f'util.files.append_import(strategy={strategy}, args={args}, '
              f'suffix_new_line={suffix_new_line})')
    log.debug(f'util.files.append_import RETURNED STUBBED {append_to}')
    return append_to  # TODO


def generate_file_text(file_node: ImportNode, prefix_new_line: bool = True,
                       append_to: str='') -> str:
    log.debug(f'util.files.generate_file_text(file_node={file_node}, '
              f'prefix_new_line={prefix_new_line}, append_to={append_to})')

    file_text = append_to

    if not file_node.is_file():
        raise Exception('Cannot generate file_text when type is'
                        f'{file_node.element_type}')

    # Header
    if hasattr(file_node, PARSING_DICT['files']['header']):
        log.debug(f'Found header in {file_node.name}')
        file_text = append_header(file_node.header,
                                  prefix_new_line=prefix_new_line)
    else:
        log.debug(f'Found NO header in {file_node.name}')
        file_text = append_header(file_node.name,
                                  prefix_new_line=prefix_new_line)

    # Text
    if hasattr(file_node, PARSING_DICT['files']['text']):
        log.debug(f'Found text in {file_node.name}')
        file_text = append_text(file_node.text, append_to=file_text,
                                prefix_new_line=prefix_new_line)

    # Import
    if hasattr(file_node, PARSING_DICT['import_strategy']):
        log.debug(f'Found import in {file_node.name}')
        try:
            file_text = append_import(strategy=file_node.import_strategy,
                                      args=file_node.import_args,
                                      append_to=file_text,
                                      suffix_new_line=prefix_new_line)
        except AttributeError as e:
            error_str: f'Invalid Import: Missing arguments' \
                       f'(file_node={file_node}, AttributeError={e})'
            log.error(error_str)
            raise AttributeError(error_str)  # TODO Attempt to handle this

    log.debug(f'generate_file_text RETURNED {file_text}')
    return file_text


if __name__ == '__main__':
    pass
