import os


def generate(name, root):
    print('Called generate with params: ', name, root)


def _ensure_string(obj):
    if isinstance(obj, str):
        return obj
    else:
        return str(obj)  # TODO regrex expression to test this


# TODO turn the working directory variable into a Python Property
class WorkingDirectory:
    def __init__(self, root='.', separator='/'):
        print('CONSTRUCTOR: WorkingDirectory'
              '\n  root: {0} type: {1},'
              '\n  separator: {2} type: {3}'
              .format(root, type(root), separator, type(separator)))
        self.root = _ensure_string(root)
        self.separator = _ensure_string(separator)
        self.directories = []
        self.relative_dir = self._gen_dir(self.directories)

    def pop(self) -> str:
        if self.size() == 0:
            print('!!!!              WARNING                             !!!!!'
                  '\n Called pop when size was zero. Returned: '
                  .format(self.root))
            return self.root

        to_return = self.directories.pop()
        self.relative_dir = self._gen_dir(self.directories)
        print('  new dir: ' + self.relative_dir)
        return to_return

    def push(self, to_append):
        print('  pushing: ', to_append)
        _dir = _ensure_string(to_append)
        self.directories.append(_dir)
        self.relative_dir = self._gen_dir(self.directories)
        print('  new dir: ' + self.relative_dir)

    def size(self):
        return len(self.directories)

    def get_dir(self) -> str:
        print('  returned dir: ' + self.relative_dir)
        return self.relative_dir

    def _gen_dir(self, directories):
        print('   called _gen_dir({0})'.format(directories))
        _str = self.root + self.separator + self.separator.join(directories)
        print('   generated working directory string as ' + _str)
        return _str
