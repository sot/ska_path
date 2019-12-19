# Licensed under a 3-clause BSD style license - see LICENSE.rst
from setuptools import setup


setup(name='ska_path',
      use_scm_version=True,
      setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
      description='Get Ska root directory',
      author='Tom Aldcroft',
      author_email='taldcroft@head.cfa.harvard.edu',
      packages=['ska_path'],
      )
