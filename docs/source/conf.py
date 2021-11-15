# -*- coding: utf-8 -*-
#
# sample documentation build configuration file,
# inspried by slabbe configuration file created sphinx-quickstart
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# General information about the project.
project = u"AVIsogenies"
copyright = u'2021, Anna Somoza'
package_name = 'avisogenies_sage'
package_folder = "../../avisogenies_sage"
authors = u"Anna Somoza"

import six
import sys
import os
from sage.env import SAGE_DOC_SRC, SAGE_DOC, SAGE_SRC

try:
    import sage.all
except ImportError:
    raise RuntimeError("to build the documentation you need to be inside a Sage shell (run first the command 'sage -sh' in a shell")




# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(package_folder))
#sys.path.append(os.path.join(SAGE_SRC, "sage_setup", "docbuild", "ext"))


print("Using sys.path = {}".format(sys.path))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.extlinks',
    'matplotlib.sphinxext.plot_directive',
    'myst_parser',
    'sphinx.ext.todo',
    'nbsphinx'
]

# Display todos by setting to True
todo_include_todos = True

# List autodoc in source order
autodoc_member_order = 'bysource'

### from Sage src/doc/common/conf.py
# This code is executed before each ".. PLOT::" directive in the Sphinx
# documentation. It defines a 'sphinx_plot' function that displays a Sage object
# through matplotlib, so that it will be displayed in the HTML doc.
plot_html_show_source_link = False
plot_pre_code = """
def sphinx_plot(graphics, **kwds):
    import matplotlib.image as mpimg
    from sage.misc.temporary_file import tmp_filename
    import matplotlib.pyplot as plt
    ## Option handling is taken from Graphics.save
    try:
        from sage.plot.multigraphics import GraphicsArray
    except ImportError:
        from sage.plot.graphics import GraphicsArray
    options = dict()
    if not isinstance(graphics, GraphicsArray):
        options.update(graphics.SHOW_OPTIONS)
        options.update(graphics._extra_kwds)
    options.update(kwds)
    dpi = options.pop('dpi', None)
    transparent = options.pop('transparent', None)
    fig_tight = options.pop('fig_tight', None)
    figsize = options.pop('figsize', None)
    ## figsize handling is taken from Graphics.matplotlib()
    if figsize is not None and not isinstance(figsize, (list, tuple)):
        # in this case, figsize is a number and should be positive
        try:
            figsize = float(figsize) # to pass to mpl
        except TypeError:
            raise TypeError("figsize should be a positive number, not {0}".format(figsize))
        if figsize > 0:
            default_width, default_height=rcParams['figure.figsize']
            figsize=(figsize, default_height*figsize/default_width)
        else:
            raise ValueError("figsize should be positive, not {0}".format(figsize))

    if figsize is not None:
        # then the figsize should be two positive numbers
        if len(figsize) != 2:
            raise ValueError("figsize should be a positive number "
                             "or a list of two positive numbers, not {0}".format(figsize))
        figsize = (float(figsize[0]),float(figsize[1])) # floats for mpl
        if not (figsize[0] > 0 and figsize[1] > 0):
            raise ValueError("figsize should be positive numbers, "
                             "not {0} and {1}".format(figsize[0],figsize[1]))

    plt.figure(figsize=figsize)
    if isinstance(graphics, GraphicsArray):
        ## from GraphicsArray.save
        figure = plt.gcf()
        rows = graphics.nrows()
        cols = graphics.ncols()
        for i, g in enumerate(graphics):
            subplot = figure.add_subplot(rows, cols, i + 1)
            g_options = copy(options)
            g_options.update(g.SHOW_OPTIONS)
            g_options.update(g._extra_kwds)
            g_options.pop('dpi', None)
            g_options.pop('transparent', None)
            g_options.pop('fig_tight', None)
            g.matplotlib(figure=figure, sub=subplot, **g_options)
    else:
        figure = graphics.matplotlib(figure=plt.gcf(), figsize=figsize, **options)
    plt.tight_layout(pad=0)
    plt.margins(0)
    plt.show()

from sage.all_cmdline import *
"""

plot_html_show_formats = False
plot_formats = ['svg', 'pdf', 'png']

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']
templates_path = [os.path.join(SAGE_DOC_SRC, 'common', 'templates'), '_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'



# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
from pkg_resources import get_distribution, DistributionNotFound
# The full version, including alpha/beta/rc tags.
try:
    release = get_distribution('sage-numerical-interactive-mip').version
except DistributionNotFound:
    release = "0.2"
#print("############# release reported: {} ##################".format(release))
# The short X.Y version.
version = '.'.join(release.split('.')[:2])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = 'math'

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []   #['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = package_name + "doc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', package_name + '.tex', u'Documentation of ' + six.text_type(package_name),
   authors, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', package_name, six.text_type(package_name) + u" documentation",
     [authors], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', package_name, six.text_type(package_name) + u" documentation",
   authors, package_name, project,
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# -- Options copied from Sagemath conf.py file -------------------------------

# We use MathJax to build the documentation unless the environment
# variable SAGE_DOC_MATHJAX is set to "no" or "False".  (Note that if
# the user does not set this variable, then the script sage-env sets
# it to "True".)

if (os.environ.get('SAGE_DOC_MATHJAX', 'no') != 'no'
            and os.environ.get('SAGE_DOC_MATHJAX', 'no') != 'False'):

    extensions.append('sphinx.ext.mathjax')
    mathjax_path = 'MathJax.js?config=TeX-AMS_HTML-full,../mathjax_sage.js'

    from sage.misc.latex_macros import sage_mathjax_macros
    # this is broken for now
    # html_theme_options['mathjax_macros'] = sage_mathjax_macros()

    ## from pkg_resources import Requirement, working_set
    ## sagenb_path = working_set.find(Requirement.parse('sagenb')).location
    ## mathjax_relative = os.path.join('sagenb','data','mathjax')

    ## # It would be really nice if sphinx would copy the entire mathjax directory,
    ## # (so we could have a _static/mathjax directory), rather than the contents of the directory

    ## mathjax_static = os.path.join(sagenb_path, mathjax_relative)
    ## html_static_path.append(mathjax_static)
    ## exclude_patterns=['**/'+os.path.join(mathjax_relative, i) for i in ('docs', 'README*', 'test',
    ##                                                                     'unpacked', 'LICENSE')]
    ## from sage.env import SAGE_LOCAL, SAGE_SHARE
    ## html_static_path.append(SAGE_LOCAL + "/lib/mathjax")    # conda
    ## html_static_path.append(SAGE_SHARE + "/mathjax")  # sage distribution
else:
     extensions.append('sphinx.ext.imgmath')

# This is to make the verbatim font smaller;
# Verbatim environment is not breaking long lines
from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter

class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\footnotesize"

PygmentsBridge.latex_formatter = CustomLatexFormatter

latex_elements['preamble'] += r'''
% One-column index
\makeatletter
\renewenvironment{theindex}{
  \chapter*{\indexname}
  \markboth{\MakeUppercase\indexname}{\MakeUppercase\indexname}
  \setlength{\parskip}{0.1em}
  \relax
  \let\item\@idxitem
}{}
\makeatother
\renewcommand{\ttdefault}{txtt}
'''

#####################################################
# add LaTeX macros for Sage

from sage.misc.latex_macros import sage_latex_macros

try:
    pngmath_latex_preamble  # check whether this is already defined
except NameError:
    pngmath_latex_preamble = ""

for macro in sage_latex_macros():
    # used when building latex and pdf versions
    latex_elements['preamble'] += macro + '\n'
    # used when building html version
    pngmath_latex_preamble += macro + '\n'

autodoc_member_order = 'bysource'

## The following is needed on conda-forge sagemath
from sage.repl.user_globals import initialize_globals
import sage.all
my_globs = dict()
initialize_globals(sage.all, my_globs)
