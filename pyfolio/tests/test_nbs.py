#!/usr/bin/env python
"""
simple example script for running notebooks and reporting exceptions.
Usage: `checkipnb.py foo.ipynb [bar.ipynb [...]]`
Each cell is submitted to the kernel, and checked for errors.
"""

import os
import glob
from runipy.notebook_runner import NotebookRunner
from IPython.nbformat.current import read

from pyfolio.utils import pyfolio_root


def test_nbs():
    path = os.path.join(pyfolio_root(), 'examples', '*.ipynb')
    for ipynb in glob.glob(path):
        with open(ipynb) as f:
            nb = read(f, 'json')
            nb_runner = NotebookRunner(nb)
            nb_runner.run_notebook(skip_exceptions=False)
