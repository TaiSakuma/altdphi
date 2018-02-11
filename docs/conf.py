# -*- coding: utf-8 -*-
#
##__________________________________________________________________||
import os
import sys
cwd = os.path.abspath('.')
sys.path.insert(0, cwd)
sys.path.insert(0, os.path.dirname(cwd))
del cwd

import recommonmark
from recommonmark.transform import AutoStructify

##__________________________________________________________________||
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}

source_suffix = ['.rst', '.md']

master_doc = 'contents'

project = u'altdphi'
copyright = u'2018, Tai Sakuma'
author = u'Tai Sakuma'

github_doc_root = 'https://github.com/TaiSakuma/altdphi/tree/master/docs'

import altdphi
version = '.'.join(altdphi.__version__.split('.')[0:2])
# e.g., '0.1'

release = '.'.join(altdphi.__version__.split('.')[0:3])
# e.g., '0.1.0'

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

todo_include_todos = True


##__________________________________________________________________||
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]

html_theme_options = {
    # 'typekit_id': hiw1hhg,
    # 'canonical_url':
    # 'analytics_id':
    'collapse_navigation': False,
    'sticky_navigation': False,
    'navigation_depth': 4,
    # 'includehidden': True,
    # 'logo_only':
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
}

html_static_path = ['_static']

##__________________________________________________________________||
htmlhelp_basename = 'altdphidoc'

##__________________________________________________________________||
latex_elements = {
}

latex_documents = [
    (master_doc, 'altdphi.tex', u'altdphi Documentation',
     u'Tai Sakuma', 'manual'),
]


##__________________________________________________________________||
man_pages = [
    (master_doc, 'altdphi', u'altdphi Documentation',
     [author], 1)
]

##__________________________________________________________________||
texinfo_documents = [
    (master_doc, 'altdphi', u'altdphi Documentation',
     author, 'altdphi', 'One line description of project.',
     'Miscellaneous'),
]

##__________________________________________________________________||
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)

##__________________________________________________________________||
