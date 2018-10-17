import tempfile
import os, shutil
from xml.etree.ElementTree import Element

class TempHandler(object):
    def __init__(self, name: str, destination):
        self.name = name
        self.destination = destination
        self.dir = tempfile.mkdtemp()
        print("Initialized temp directory at {}".format(self.dir))

    def generate_dir(self, cur: Element, root=None) -> object:
        print("generating directory {0}, from root {1}".format(cur.tag, root))

        if root is None:
            print("root was none")
            path = os.path.join(self.dir, cur.tag)
        else:
            print("root is: ", root)
            path = os.path.join(self.dir, root, cur.tag)

        print("attempting to create a directory at {0}".format(path))
        return os.mkdir(path)

    def generate_file(self, cur: Element, path):
        return tempfile.mkstemp(dir=path, text=True, suffix=cur.tag)

    def finalize(self):
        shutil.copytree(self.dir, self.destination)

