# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ipstore'
copyright = '2025, 迪普希'
author = '迪普希'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              ] # <- 这个

templates_path = ['_templates']
exclude_patterns = []

language = 'zh-cn'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
  # canonical_url is deprecated for html_baseurl
  'analytics_id': '',
  'logo_only': False,
  'prev_next_buttons_location': 'bottom',
  'style_external_links': False,
  # Toc options
  'collapse_navigation': False,
  'sticky_navigation': True,
#    'navigation_depth': 4,
  'includehidden': True,
  'titles_only': False
}
