# -*- coding: utf-8 -*-
#
# Spyder documentation build configuration file, created by
# sphinx-quickstart on Fri Jul 10 16:32:25 2009.
#
# This file is execfile()d with the current directory set to its parent dir.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from docutils import nodes
from docutils.parsers.rst import Directive, directives

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

# Standard library imports
import os

# import sys
# sys.path.insert(0, os.path.abspath('.'))

# Constants
CI = os.environ.get("CI")
TRAVIS_BRANCH = os.environ.get("TRAVIS_BRANCH")

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.githubpages",
    "sphinx_panels",
    "sphinx_multiversion"
]

panels_add_boostrap_css = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The encoding of source files.
source_encoding = "utf-8"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Spyder"
copyright = " 2020 Spyder Doc Contributors <a href='https://opensource.org/licenses/MIT' target='_blank'>MIT License</a>"
author = "The Spyder Doc Contributors"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "4"
# The full version, including alpha/beta/rc tags.
release = "4"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
# unused_docs = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all docs.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# CI = True
# TRAVIS_BRANCH = 'master'
html_theme = "pandas_sphinx_theme"
html_logo = '_static/spyder_logo.png'
html_theme_options = {
    "external_links": [
        {
            "url": "https://www.spyder-ide.org",
            "name": "Home"
        },
        {
            "url": "https://www.spyder-ide.org/blog",
            "name": "Blog"
        }
    ],
    "use_edit_page_button": True,
    "show_powered_by": True,
    "gitter_room": "spyder-ide/public",
    "open_collective": "spyder",
    "footer_links": [
        {
            "url": "https://github.com/spyder-ide/spyder",
            "name": "GitHub",
        },
        {
            "url": "https://twitter.com/Spyder_IDE",
            "name": "Twitter",
        },
        {
            "url": "https://www.facebook.com/SpyderIDE/",
            "name": "Facebook",
        },
        {
            "url": "https://www.youtube.com/channel/UCAOyvaOj7dMnavvGUkz9Djg",
            "name": "YouTube",
        },
        {
            "url": "https://instagram.com/spyderide",
            "name": "Instagram",
        },
        {
            "url": "https://groups.google.com/group/spyderlib",
            "name": "Google Groups",
        },
    ],
    "page_toc_limit": 1,
}
html_context = {
    "github_user": "spyder-ide",
    "github_repo": "spyder-docs",
    "github_version": "master",
    "doc_path": "doc",
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = 'spyder_bbg.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom CSS for the site
html_css_files = [
    "driver.min.css",
    "custom_styles.css",
]

# Custom Javascript for the site
html_js_files = [
    "driver.min.js",
    "custom_scripts.js",
]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {
#     "**": [
#         "about.html",
#         "navigation.html",
#         #'relations.html',
#         "searchbox.html",
#         "donate.html",
#     ]
# }

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_use_modindex = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''


# -- Options for shpinx-multiversion -----------------------------------------

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = r'\d+\.\w|(master)$'

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = None


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Spyderdoc"


# -- Options for LaTeX output ------------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ("index", "Spyder.tex", "Spyder Documentation", author, "manual"),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Spyder",
        "Spyder Documentation",
        author,
        "Spyder",
        "The Scientific Python Development Environment.",
        "Miscellaneous",
    ),
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Additional Directives ---------------------------------------------------

# ReST directive for embedding Youtube and Vimeo videos.
# There are two directives added: ``youtube`` and ``vimeo``. The only
# argument is the video id of the video to include.
# Both directives have three optional arguments: ``height``, ``width``
# and ``align``. Default height is 281 and default width is 500.
# Example::
#     .. youtube:: anwy2MPT5RE
#         :height: 315
#         :width: 560
#         :align: left
# :copyright: (c) 2012 by Danilo Bargen.
# :license: BSD 3-clause

def align(argument):
    """Conversion function for the "align" option."""
    return directives.choice(argument, ('left', 'center', 'right'))


class IframeVideo(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'height': directives.nonnegative_int,
        'width': directives.nonnegative_int,
        'align': align,
        'start': directives.nonnegative_int,
    }
    default_width = 500
    default_height = 281
    default_start = 0

    def run(self):
        self.options['video_id'] = directives.uri(self.arguments[0])
        if not self.options.get('width'):
            self.options['width'] = self.default_width
        if not self.options.get('height'):
            self.options['height'] = self.default_height
        if not self.options.get('align'):
            self.options['align'] = 'left'
        if not self.options.get('start'):
            self.options['start'] = self.default_start
        return [nodes.raw('', self.html % self.options, format='html')]


class Youtube(IframeVideo):
    html = ('<iframe src="https://www.youtube.com/embed/%(video_id)s'
            '?start=%(start)s" '
            'width="%(width)u" height="%(height)u" frameborder="0" '
            'webkitAllowFullScreen mozallowfullscreen allowfullscreen '
            'class="align-%(align)s"></iframe>')


def setup(builder):
    directives.register_directive('youtube', Youtube)
