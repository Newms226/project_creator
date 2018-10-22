import tempfile
import os, shutil
from xml.etree.ElementTree import Element
import os.path as Paths
from util.folders import WorkingDirectory as working_dir


class TempHandler(object):
    def __init__(self, destination):
        self.destination = destination
        self.dir = tempfile.mkdtemp()  # TODO auto clean up
        print("Initialized temp at {1} with plans to go to {2}"
              .format(self.dir, destination))

    def finalize(self, temp_root: str):
        print('temp_root passed: {}'.format(temp_root))  # TODO copy to root
        
