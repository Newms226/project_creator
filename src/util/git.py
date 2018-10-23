from git import Repo
from xml.etree.ElementTree import Element


class GitRepo:
    def __init__(self, url_path, destination):
        print('CONSTRUCTOR: GitRepo'
              f'\n  {url_path} -> {destination}')
        self.repo = Repo.clone_from(url_path, destination)
        self.git = self.repo.git

    def branch(self, branch_name):
        print(f' branch({branch_name})')
        new_branch = self.repo.create_head(branch_name)
        self.repo.head.reference = new_branch
        print(f'  switched to new branch: {branch_name}')
        print(f'   cur branch: {self.repo.active_branch}')


def get_git_tracking_bool(cur: Element) -> bool:
    directive = cur.get('git')
    if not directive:
        return True
    else:
        if directive == 'True':
            return True
        else:
            return False


class GitTracker:
    """ Keeps track of any files/folders which should not be tracked in a git repo
    """

    def __init__(self, import_text: str = None):
        self.tracking = []
        self.ignoring: str = []
        self.export = ''

        if import_text:
            self.export = f'# Imported to GitTracker:\n{import_text}\n'

    def register(self, path, track: bool):
        """Registers an element (either tracks or ignores)"""

        print(f'  registering: {path}')

        if track:
            self._track()
        else:
            self._ignore()

    def _track(self, path):
        print(f'   tracking {path}')
        for p in self.ignoring:
            if path in p:
                print(f'    NESTED: tracked path ({path}) found in ignored '
                      f'path ({p})')
                self._nested_track(path)
                return

        # self.tracking.append(path)

    def _nested_track(self, path):
        print(f'   _nested_track({path})')
        self.tracking.append(path)

    def _ignore(self, path):
        print(f'   ignoring {path}')

        for p in self.ignoring:
            if p.startswith(path):
                print(f'    SKIPPED: ({path}) was found to be a sub directory '
                      f'of ({p})')
                return

        self.ignoring.append(path)

    def get_git_ignore(self) -> str:
        """returns the contents of self.ignoring as a valid str"""

        self.export += f'\n\n# Ignore (generated by {__name__}):' \
                       f'\n{self._get_ignore_text()}' \
                       f'\n\n# Nested tracking (generated by {__name__}):' \
                       f'\n{self._get_nested_text()}'
        # print('GITIGNORE:'
        #      f'\n{_str}')

        return self.export

    def _get_ignore_text(self) -> str:
        _str = ''

        for ignored in self.ignoring:
            _str += ignored + '\n'

        return _str

    def _get_nested_text(self) -> str:

        _str = ''

        for tracked in self.tracking:
            _str += '!' + tracked + '\n'

        return _str