# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Utility function to find file paths in the Ska environment.
"""
import os
from pathlib import Path

__all__ = ['ska_path']


def ska_path(*path_args):
    """
    Return the path corresponding to supplied ``args`` relative to
    the SKA environment variable path.

    This returns a Path object or None if the path does not exist and
    exists=False.

    Examples::

      >>> from ska_path import ska_path
      >>> AGASC_DATA = ska_path('data', 'agasc')
      >>> ska_path('data', 'blah')
      FileNotFoundError('/proj/sot/ska/data/blah not found')

    :param *path_args: zero, one or more path strings

    :returns: Path object or None
    """
    ska = os.environ.get('SKA')
    if ska is None:
        raise ValueError('SKA environment must be defined to get path')

    path = Path(ska).joinpath(*path_args)
    if not path.exists():
        raise FileNotFoundError(f"No such file or directory: '{path}'")

    return path
