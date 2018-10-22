# from git import Repo
from xml.etree.ElementTree import Element


class GitTracker:
    """ Keeps track of any files/folders which should not be tracked in a git repo
    """

    def __init__(self):
        self.tracking = []
        self.ignoring = []

    def register(self, cur: Element, path):
        """Registers an element (either tracks or ignores)"""

        print(f'  registering {cur.tag} @ {path}')
        directive = cur.get('git')

        if not directive:
            self._track(cur, path)
        else:
            if directive == 'True':
                self._track(cur, path)
            else:
                self._ignore(cur, path)

    def _track(self, cur: Element, path):
        print(f'   tracking {cur.tag} @ {path}')
        self.tracking.append(path)

    def _ignore(self,cur: Element, path):
        print(f'   ignoring {cur.tag} @ {path}')
        self.ignoring.append(path)

    def get_git_ignore(self) -> str:
        """returns the contents of self.ignoring as a valid str"""
        _str = ''

        for path in self.ignoring:
            _str = _str + path + '\n'

        # print('GITIGNORE:'
        #      f'\n{_str}')

        return _str
