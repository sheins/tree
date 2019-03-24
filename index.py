"""Usage:
  sudowoodo show <directory>
  sudowoodo -h | --help | --version

Options:
  directory  Which directory to show.
  -h --help  Show this screen.
"""

from docopt import docopt

args = docopt(doc=__doc__)
