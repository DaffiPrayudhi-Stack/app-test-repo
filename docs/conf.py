# -*- coding: utf-8 -*-
import os
import sys
from datetime import datetime

# Add project root to path untuk autodoc
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../application'))

# -- Project information -----------------------------------------------------
project = 'SSM Project'
copyright = f'{datetime.now().year}, Sinar Sakti'
author = 'SSM'

release = '1.0.0'
version = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',
    'sphinx_design',
]

# Napoleon settings untuk Google-style docstrings
napoleon_google_docstring = True
napoleon_include_init_with_doc = True

# Template settings
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

# Theme options
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'style_nav_header_background': '#2980b9',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# -- Options for TODO extension ----------------------------------------------
todo_include_todos = True