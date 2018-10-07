# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Adlbx(AutotoolsPackage):
    """ADLB/X: Master-worker library + work stealing and data dependencies"""

    homepage = 'http://swift-lang.org/Swift-T'
    url      = 'http://swift-lang.github.io/swift-t-downloads/adlbx-0.8.0.tar.gz'
    version('0.8.0', '34ade59ce3be5bc296955231d47a27dd')

    depends_on('exmcutils')
    depends_on('mpi')

    def configure_args(self):
        args = ['--with-c-utils=' + self.spec['exmcutils'].prefix]
        return args
