from os import path as Paths

def generate_reST_header(title: str, underline_with_char: str = '#',
                         top: bool = False) -> str:
    header = ''
    i = 0
    while i < len(title):
        header += underline_with_char
        i = i + 1

    _str = ''
    if top:
        _str = header + '\n'

    _str = _str + title + '\n' + header
    return _str


def write_text(path, text: str, close: bool = True):
    _file = open(path, 'w+')
    _file.write(text)

    if close:
        _file.close()
    else:
        return _file


def make_file(path: str, name: str, suffix:str):
    print(f'   make_file(path={path}, name={name}, suffix={suffix})')

    filename = name + suffix
    print(f'    file name generated as {filename}')

    abs_path = Paths.join(path, filename)
    print(f'    path={abs_path}')

    open(abs_path, 'w+').close()  # TODO write file text!
