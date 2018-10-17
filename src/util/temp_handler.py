import tempfile
import os, shutil
from xml.etree.ElementTree import Element
import os.path as Paths


class TempHandler(object):
    def __init__(self, name: str, destination):
        self.name = name
        self.destination = destination
        self.dir = tempfile.mkdtemp()
        print("Initialized name: {0}\nat {1}\nwith plans to go to {"
              "2}".format(name, self.dir, destination))

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

    def generate_file(self, cur: Element, root=None):
        print("generating file {0}, from root {1}".format(cur.tag, root))
        filename = cur.tag + "." + cur.find("extension").text
        print("  filename: ", filename)

        if root is None:
            print("  root was none")
            path = os.path.join(self.dir, filename)
        else:
            print("  root is: ", root)
            path = os.path.join(self.dir, root, filename)

        print("  path is ", path)
        return os.mkdir(path)

    def finalize(self):
        print("dir: {0}, dest: {1}, name {2}".format(self.dir,
                                                     self.destination,
                                                     self.name))
        shutil.copytree(self.dir, Paths.join(self.destination, self.name))

