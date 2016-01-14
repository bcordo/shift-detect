#!/usr/bin/env python
#
# Documentation generator configuration
#
import re
import os
import sphinx_py3doc_enhanced_theme

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinxcontrib.napoleon'
]

if os.getenv('SPELLCHECK') :
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'

source_suffix         = '.rst'
master_doc            = 'index'
project               = u'Change Detector'
copyright             = u'2016, Paolo de Dios'
version               = re.findall('version="(.*)"', open(os.path.join(os.path.dirname(__file__), '../setup.py')).read())[0]
release               = version
html_theme            = "sphinx_py3doc_enhanced_theme"
html_theme_path       = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]

pygments_style        = 'trac'
templates_path        = ['.']
html_use_smartypants  = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index      = True
html_sidebars         = {
    '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title      = '%s-%s' % (project, version)
html_theme_options    = {
}
