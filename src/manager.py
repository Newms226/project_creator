from src.models import model_parser
from src.util import folders as dir_util
from src.util import git


def generate(xml_location):
    manager = model_parser.new(xml_location)
    githandler = git.GitHandler.new()

    for folder in manager.folders.iter():
        dir_util.generate(folder.get('name'), folder.get('root'))
        githandler.register(folder)

    for file in manager.files.iter():

