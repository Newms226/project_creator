from os import makedirs as _makedirs, path
from tempfile import mkdtemp
from project_creator.logging_config import root_logger as log
from project_creator.util.strings import require_string


'''def make_dir(name, root):
    _path = path.join(root, name)
    print(f' Called generate with root {root}, name: {name}')
    makedirs(_path, exist_ok=True)
    print(f' Successfully created directory at {_path}')'''


def make_folder(path_to):
    log.debug(f'({path_to})')

    if path.exists(path_to):
        log.warning(f'Attempted to make directory {path_to} when it already '
                    f'existed')
        if not path.isdir(path_to):
            exception_str = f"'{path_to}' exists & is not a directory"
            log.error(exception_str)
            raise Exception(exception_str)
    else:
        _makedirs(path_to)

    log.debug(f'RETURNED {path_to}')
    return path_to


class TempHandler(object):
    def __init__(self, destination):
        log.debug(f'INIT (destination={destination})')
        self.data = (destination, mkdtemp())
        log.debug(f'planning to go to {self.temp_dir}')

    @property
    def destination_dir(self):
        to_return = self.data[0]
        log.debug(f'PROPERTY RETURNED {to_return}')
        return to_return

    @property
    def temp_dir(self):
        to_return = self.data[1]
        log.debug(f'PROPERTY RETURNED {to_return}')
        return to_return

    def finalize(self):
        log.debug(f'STUBBED (temp_dir={self.temp_dir}, '
                  f'destination_dir={self.destination_dir})')
        # TODO: actually do the move
        # shutil.copytree(self.temp_dir, self.destination_dir)

        log.debug(f'RETURNED {self.temp_dir}')
        return self.temp_dir


# TODO turn the working directory variable into a Python Property
class WorkingDirectory:
    def __init__(self, root='.'):

        log.debug(f'INIT (root={root})')

        self._root = (require_string(root, log=log), )
        self.directories = []

    @property
    def root(self):
        log.debug(f'PROPERTY RETURNED {self._root[0]}')
        return self._root[0]

    @property
    def relative_dir(self):
        to_return = path.join('', *self.directories)
        log.debug(f'PROPERTY RETURNED {to_return}')
        return to_return

    @property
    def absolute_dir(self):
        to_return = path.join(self.root, *self.directories)
        log.debug(f'PROPERTY RETURNED {to_return}')
        return to_return

    def pop(self) -> str:
        log.debug('popping..')

        if self.size <= 0:
            log.warning(f'Called pop when size was zero.')
            to_return = self.root
        else:
            to_return = self.directories.pop()

        log.debug(f'RETURNED {to_return}')
        return to_return

    def push(self, to_append):
        log.debug(f'(to_append={to_append})')

        _dir = require_string(to_append, log=log)
        self.directories.append(_dir)

        log.debug(f'RETURNED')

    @property
    def size(self):
        return len(self.directories)
