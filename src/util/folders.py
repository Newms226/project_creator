from os import makedirs
from os import path as Paths
from warnings import warn
from util import mkdtemp


'''def make_dir(name, root):
    _path = path.join(root, name)
    print(f' Called generate with root {root}, name: {name}')
    makedirs(_path, exist_ok=True)
    print(f' Successfully created directory at {_path}')'''


def make_folder(path):
    print(f' called make_dir({path})')
    makedirs(path, exist_ok=True)
    print(f' Successfully created directory at {path}')


def _ensure_string(obj):
    if isinstance(obj, str):
        return obj
    else:
        return str(obj)  # TODO regrex expression to test this


class TempHandler(object):
    def __init__(self, destination):
        self.destination = destination
        self.dir = mkdtemp()
        print(f"Initialized temp at {self.dir} with plans to go to "
              f"{self.destination}")

    def finalize(self):
        print(f'called finalize. Temp location: {self.dir}, Planed '
              f'destination: {self.destination}')  # TODO copy to root
        # shutil.copytree(self.dir, self.destination)


# TODO turn the working directory variable into a Python Property
class WorkingDirectory:
    def __init__(self, root='.', separator='/'):
        print('CONSTRUCTOR: WorkingDirectory'
              f'\n  root: {root} type: {type(root)},'
              f'\n  separator: {separator} type: {type(separator)}')
        self.root = _ensure_string(root)
        self.separator = _ensure_string(separator)
        self.absolute_dir = self.root
        self.relative_dir = ""
        self.directories = []

    def pop(self) -> str:
        print('  popping')
        if self.size() == 0:
            warn(f'Called pop when size was zero. Returned: {self.root}')
            return self.root

        to_return = self.directories.pop()
        self._update_dir()
        print(f'  popped & returning: {to_return}')
        return to_return

    def push(self, to_append):
        print(f'  pushing: {to_append}')
        _dir = _ensure_string(to_append)
        self.directories.append(_dir)
        self._update_dir()
        print(f'  pushed: {to_append}')

    def size(self):
        return len(self.directories)

    def _update_dir(self):  # TODO use paths to join!
        self.relative_dir = self.separator.join(self.directories)
        self.absolute_dir = self.root + self.separator + self.relative_dir
        print(f'    relative_dir: {self.relative_dir}')
        print(f'    absolute_dir: {self.absolute_dir}')
