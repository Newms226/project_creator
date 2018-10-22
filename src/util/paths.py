import tempfile
import os, shutil
from xml.etree.ElementTree import Element
import os.path as Paths


class TempHandler(object):
    def __init__(self, name: str, destination):
        self.name = name
        self.destination = destination
        self.dir = tempfile.mkdtemp()
        print("Initialized name: {0}\nat {1}\nwith plans to go to {2}"
              .format(name, self.dir, destination))

    def finalize(self):
        print("dir: {0}, dest: {1}, name {2}".format(self.dir,
                                                     self.destination,
                                                     self.name))
        shutil.copytree(self.dir, Paths.join(self.destination, self.name))
