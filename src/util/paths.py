import tempfile
import os, shutil
from xml.etree.ElementTree import Element
import os.path as Paths
from util.folders import WorkingDirectory as working_dir


class TempHandler(object):
    def __init__(self, destination):
        self.destination = destination
        self.dir = tempfile.mkdtemp()  # TODO auto clean up
        print(f"Initialized temp at {self.dir} with plans to go to "
              f"{self.destination}")

    def finalize(self):
        print(f'called finalize. Temp location: {self.dir}, Planed '
              f'destination: {self.destination}')  # TODO copy to root
        # shutil.copytree(self.dir, self.destination)
