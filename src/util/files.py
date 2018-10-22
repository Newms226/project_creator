

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
    _file = open(path)
    _file.write(text)

    if close:
        _file.close()
    else:
        return _file
