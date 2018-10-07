# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PySpyder(PythonPackage):
    """Scientific PYthon Development EnviRonment"""

    homepage = "https://github.com/spyder-ide/spyder"
    url      = "https://pypi.io/packages/source/s/spyder/spyder-3.1.3.tar.gz"

    version('3.1.3', '4b9b7c8c3e6dc00001e6e98473473c36')
    version('2.3.9', 'dd01e07a77123c128ff79ba57b97c1d7')

    depends_on('py-setuptools',       type='build')
    depends_on('py-rope@0.9.4:',      type=('build', 'run'), when='^python@:3')
    # depends_on('py-rope_py3k',    type=('build', 'run'), when='^python@3:')
    depends_on('py-jedi@0.9.0',       type=('build', 'run'))
    # otherwise collision with py-flake8
    depends_on('py-pyflakes@1.2.3',   type=('build', 'run'))
    depends_on('py-pygments@2.0:',    type=('build', 'run'))
    depends_on('py-qtconsole@4.2.0:', type=('build', 'run'))
    depends_on('py-nbconvert',        type=('build', 'run'))
    depends_on('py-sphinx',           type=('build', 'run'))
    depends_on('py-pycodestyle',      type=('build', 'run'))
    depends_on('py-pylint',           type=('build', 'run'))
    depends_on('py-psutil',           type=('build', 'run'))
    depends_on('py-qtawesome@0.4.1:', type=('build', 'run'))
    depends_on('py-qtpy@1.1.0:',      type=('build', 'run'))
    depends_on('py-zmq',              type=('build', 'run'))
    depends_on('py-chardet@2:',       type=('build', 'run'))
    depends_on('py-pickleshare',      type=('build', 'run'))
    depends_on('py-numpydoc',         type=('build', 'run'))
