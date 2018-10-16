import tempfile, os.path as name_util

class TempHandler(object):
    def __init__(self, name: str, destination):
        self.name = name
        self.destination = destination
        self.dir = tempfile.mkdtemp()

    def generate_directory(self, path):
        return tempfile.mkdtemp(dir=name_util.join(self.dir, path))

    def generate_file(self, name:str, extension:str):
        return tempfile.mkstemp(dir=self.dir, prefix=name,
                                suffix= ".".join(extension))
