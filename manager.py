import os
import config
from util import git



class Project:

    def __init__(self, name, root_dir = os.curdir):
        self.project_name = name
        self.root_dir = root_dir

    ''' Auto performs the creation of a project directory
    
    Process
    1. if *git* is set to ``True``, initalize the git repo
    '''
    def auto(self, name: str, model, repo=True, clone=False,
             directory=os.curdir, temp=True,
             auto_combine=True, url_root=config.DEFAULTS['URL_ROOT']):
        if repo:
            git.auto_gen(name, temp, directory, repo, auto_combine, url_root)






# TODO remote?
