# -*- coding: utf-8 -*-

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'app-test-repo-doc'
copyright = '2025, Daffi Prayudhi'
author = 'Daffi Prayudhi'

# The full version, including alpha/beta/rc tags
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

# TAMBAHKAN MASTER DOC SETTING:
master_doc = 'index'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']