import os
from util import git as repo
import config


class Project:

    def __init__(self, name, root_dir = os.curdir):
        self.project_name = name
        self.root_dir = root_dir

    ''' Auto performs the creation of a project directory
    
    Process
    1. if *git* is set to ``True``, initalize the git repo
    '''
    def auto(self, name:str, model, git=True, init=True, clone=False,
             directory=os.curdir,
             auto_combine=True, URL_Root=config.DEFAULTS['URL_ROOT']):
        if git:





# TODO remote?
