class SyncHandler(object):
    def __init__(self, git_track: bool = True):
        self._git_track = git_track

    @property
    def git_track(self):
        return self._git_track