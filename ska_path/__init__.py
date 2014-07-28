import os
import sys

__all__ = ['root_path', 'ska_path']


def root_path():
    return os.path.abspath(os.sep)


def ska_path():
    ska = os.environ.get('SKA')
    if ska is not None:
        return ska
    homevar = 'HOMEPATH' if sys.platform.startswith('win') else 'HOME'
    root = root_path()
    for path in (os.path.join(root, 'proj', 'sot', 'ska'),
                 os.path.join(os.environ.get(homevar, root), 'ska')):
        if os.path.exists(path):
            return path

    raise IOError('No Ska root directory found')
