import sphinx_rtd_theme

project = 'Botium'
copyright = '2020, Botium'
author = 'Botium'
version = '1.x'
extensions = [ 'sphinx_rtd_theme' ]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = "sphinx_rtd_theme"
html_theme_options = {
  "logo_only": True
}
html_logo = '_static/botium-120x33.png'
html_static_path = ['_static']