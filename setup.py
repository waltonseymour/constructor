# (c) 2016 Continuum Analytics, Inc. / http://continuum.io
# All Rights Reserved
#
# constructor is distributed under the terms of the BSD 3-clause license.
# Consult LICENSE.txt or http://opensource.org/licenses/BSD-3-Clause.

import re
import sys
from os.path import abspath, join
from distutils.core import setup


# read version from constructor/__init__.py
pat = re.compile(r'__version__\s*=\s*(\S+)', re.M)
data = open(join('constructor', '__init__.py')).read()
version = eval(pat.search(data).group(1))

setup(
    name = "constructor",
    version = version,
    author = "Ilan Schnell",
    author_email = "ilan@continuum.io",
    url = "https://github.com/conda/constructor",
    license = "BSD",
    description = "create installer from conda packages",
    long_description = open('README.md').read(),
    packages = ['constructor', 'constructor.tests'],
    scripts = ['bin/constructor'],
)
