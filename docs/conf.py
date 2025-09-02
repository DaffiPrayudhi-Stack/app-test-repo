# -*- coding: utf-8 -*-
import os
import sys

# Tambahkan path ke sistem
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../application'))

# -- Project information -----------------------------------------------------
project = 'FingerPrint Access'
copyright = '2025, SSM'
author = 'Sinar Sakti'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.napoleon',
    'sphinxcontrib.phpdomain',
]

# Template dan theme
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

# -- Options for TODOs -------------------------------------------------------
todo_include_todos = True