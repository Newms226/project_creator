ELEMENTS = [
    {
        'path': '/Users/michael/prog/python/python3/project_creator/test/resources/'
                'file_parse_base.xml',
        'type': 'XML',
        'elements': {
            'folder_root/src': {
                'name': 'src',
                'git': True,
                'depth': 2,
                'type': 'folder',
                'parent': None,
                'is_folder': True,
                'is_file': False
            },
            'folder_root/design': {
                'name': 'design',
                'git': True,
                'depth': 2,
                'type': 'folder',
                'parent': None,
                'is_folder': True,
                'is_file': False,
                'children': ['agile']
            },
            'folder_root/design/agile': {
                'name': 'agile',
                'git': True,
                'depth': 2,
                'type': 'folder',
                'parent': None,
                'is_folder': True,
                'is_file': False,
                'children': ['project_backlog', 'sprint_backlog']
            },
            'folder_root/venv': {
                'name': 'venv',
                'git': False,
                'depth': 2,
                'type': 'folder',
                'is_folder': True,
                'is_file': False
            },
            'folder_root/README': {
                'name': 'README',
                'git': True,
                'depth': 2,
                'type': 'file',
                'is_folder': False,
                'is_file': True,
                'extension': 'txt',
                'header': 'Readme',
                'text': 'This is the readme',
                'file_contents': 'Readme\n=======\nThis is the readme',
                'prefix_new_line': True
            },
            'folder_root/design/agile/sprint_backlog': {
                'name': 'sprint_backlog',
                'git': False,
                'depth': 3,
                'type': 'file',
                'is_folder': False,
                'is_file': True,
                'extension': 'rst',
                'header': 'Sprint Backlog',
                'text': '#. design',
                'file_contents': 'Sprint Backlog\n===============\n#. design',
                'prefix_new_line': True
            },
            'folder_root/design/agile/project_backlog': {
                'name': 'project_backlog',
                'git': True,
                'depth': 3,
                'type': 'file',
                'is_folder': False,
                'is_file': True,
                'extension': 'rst',
                'header': 'Project Backlog',
                'file_contents': 'Project Backlog\n================',
                'prefix_new_line': True
            }
        }
    }
]

INFO = [
    {
        'path': '/Users/michael/prog/python/python3/project_creator/test/'
                'resources/file_parse_base.xml',
        'type': 'XML',
        'elements': {
            'meta': {
                'name': 'Project Creator',
                'root_dir': '/Users/Michael/prog/python/python3',
                'date': {
                    'month': '10',
                    'day': '5',
                    'year': '2018'
                },
                'license': 'MIT'
            },
            'language': {
                'type': 'Python',
                'version': '3.7'
            }
        }
    }
]