from models.config import configparser


class CONFIG(object):

    def __init__(self, ):
        self.file_separator
        self.folder_separator
        self.config_locations: tuple
        self.project_dict: dict
        self.user_dict: dict
        self.language_tuple: tuple
        self.xml_parsing_dict: dict



def get_config(project_ini, git_ini, sync_ini, delimiter: str = ':',
             allow_no_value: bool = True):
    config_locations = (project_ini, git_ini, sync_ini)

