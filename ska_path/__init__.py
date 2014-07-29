"""
Utility function to find file paths in the Ska environment.
"""
import os
import sys

__all__ = ['root_path', 'ska_path']


def root_path():
    return os.path.abspath(os.sep)


def ska_path(*path_args, **kwargs):
    """
    Return the path corresponding to supplied ``args`` in the Ska
    environment root.

    The first option of the following which exists is returned:

    - SKA environment variable / *path_args
    - /proj/sot/ska / *path_args
    - HOME_DIRECTORY / ska / *path_args
    - . / *path_args

    If none exist then None is returned if ``raise`` is False (default),
    otherwise an IOError exception is raised.

    Examples::

      >>> from ska_path import ska_path
      >>> AGASC_DATA = ska_path('data', 'agasc')
      >>> ska_path()
      '/proj/sot/ska'
      >>> ska_path('data', 'blah', require_match=True)
      IOError: Could not find data/blah in any valid Ska path

    :param *path_args: zero, one or more path strings
    :param require_match: bool, if True then require a matching path
    :returns: path or None (if require_match=False)
    """
    paths = []

    ska = os.environ.get('SKA')
    if ska is not None:
        paths.append(os.path.join(ska, *path_args))

    homevar = 'HOMEPATH' if sys.platform.startswith('win') else 'HOME'
    root = root_path()

    paths.append(os.path.join(root, 'proj', 'sot', 'ska', *path_args))
    paths.append(os.path.join(os.environ.get(homevar, root), 'ska', *path_args))
    paths.append(os.path.join('', *path_args))

    for path in paths:
        if os.path.exists(path):
            return path

    if kwargs.get('require_match'):
        raise IOError('Could not find {} in any valid Ska path'
                      .format(os.path.join(*path_args)))
    else:
        return None
