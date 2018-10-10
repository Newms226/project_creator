import os, requests, config
from urllib import parse
from util import directories

def clone(rootDir:str = os.curdir ):
    # TODO write method


def branch(name:str, parent:str="master"):
    # TODO write method


def do_init(repo_directory=os.curdir):
    if not repo_directory == os.curdir:  # TODO cd to directory
    # TODO write method


def add(*files)
    if files == None: '''git add .'''
    else: '''git add + files.join'''
    # TODO write method

def commit(message):
# TODO write method


def push():
# TODO write method

def render_url(name, URL_root = 'https://github.com/Newms226/')
    return parse.urljoin(URL_root, name)

def valid_repo_url(url):
    return requests.get(url).status_code < 400

''' Ensures that the url

Raises:
    Exception: If URL is not a from github
    ConnectionError: If url cannot be accessed via an Apache Request
'''
def assert_valid_repo(url):
    if not valid_git_hub_url(url): raise Exception('Is not from GitHub: %s'
                                                   % url)
    if not valid_repo_url(url): raise ConnectionError('Is not accessible: '
                                                      '%s' % url)

def valid_git_hub_url(url):
    return str(url).index('https://github.com/') == 0

def auto_gen(name, temp=False, root_directory=os.curdir, init_repo=True,
             auto_combine=True, url_root=config.DEFAULTS['URL_ROOT'],
             ):
    if auto_combine:
        qualified_url = render_url(name, url_root)
    if url_root is not config.DEFAULTS['URL_ROOT']:
        assert_valid_repo(qualified_url)


    if init_repo:
        if not directories.exsits(root_directory):
            if temp:
                repo_dir = directories.create_temp(root_directory)
            else:
                repo_dir = directories.create(root_directory)

        do_init(repo_dir)





# TODO error handler