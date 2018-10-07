# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Cube(AutotoolsPackage):
    """Cube the profile viewer for Score-P and Scalasca profiles. It displays a
    multi-dimensional performance space consisting of the dimensions:
    - performance metric
    - call path
    - system resource
    """

    homepage = "http://www.scalasca.org/software/cube-4.x/download.html"
    url = "http://apps.fz-juelich.de/scalasca/releases/cube/4.4/dist/CubeBundle-4.4.tar.gz"

    version('4.4',   'f4f0544883bdd5bad9e11a4a692858bf')
    version('4.3.5', 'e5dce986e3c6381ea3a5fcb66c553adc')
    version('4.3.4', '50f73060f55311cb12c5b3cb354d59fa')
    version('4.3.3', '07e109248ed8ffc7bdcce614264a2909')

    version('4.2.3', '8f95b9531f5a8f8134f279c2767c9b20')

    variant('gui', default=False, description='Build CUBE GUI')

    patch('qt-version.patch', when='@4.3.0:4.3.999 +gui')

    depends_on('zlib')

    depends_on('qt@5:', when='@4.3.0: +gui')
    depends_on('qt@4.8:', when='@4.2.0:4.2.999 +gui')

    def url_for_version(self, version):
        if version >= Version('4.4'):
            filename = 'CubeBundle-{0}.tar.gz'.format(version)
        else:
            filename = 'cube-{0}.tar.gz'.format(version)

        return 'http://apps.fz-juelich.de/scalasca/releases/cube/{0}/dist/{1}'.format(version.up_to(2), filename)

    def configure_args(self):
        spec = self.spec

        configure_args = ['--enable-shared']

        if '+gui' not in spec:
            configure_args.append('--without-gui')

        return configure_args

    def install(self, spec, prefix):
        make('install', parallel=False)
