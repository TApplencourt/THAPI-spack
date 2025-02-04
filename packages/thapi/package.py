# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class Thapi(AutotoolsPackage):
    """A tracing infrastructure for heterogeneous computing applications."""

    homepage = "https://github.com/argonne-lcf/THAPI"
    git      = "https://github.com/argonne-lcf/THAPI.git"

    version('master', branch='master', preferred=True)

    depends_on('automake', type=('build'))
    depends_on('autoconf', type=('build'))
    depends_on('libtool', type=('build'))
    #depends_on('babeltrace@1.5.8:', type=('build', 'link', 'run'))
    depends_on('babeltrace2', type=('build', 'link', 'run'))
    depends_on('protobuf@3.0.0:', type=('build', 'link', 'run'))
    depends_on('lttng-ust@2.12.0', type=('build', 'link', 'run'))
    depends_on('lttng-tools@2.12.0', type=('build', 'link', 'run'))
    depends_on('ruby@2.3.0:', type=('build', 'run'))
    #depends_on('ruby-babeltrace', type=('build', 'run'))
    depends_on('ruby-babeltrace2', type=('build', 'run'))
    depends_on('ruby-opencl', type=('build', 'run'))
    depends_on('ruby-nokogiri', type=('build'))
    depends_on('ruby-cast-to-yaml', type=('build'))
    depends_on('libiberty+pic')
    depends_on('libffi')
    depends_on('pkgconfig')

    variant('strict', default=False, description='Enable -Werror during the build')
    def configure_args(self):
        args = []
        args.extend(self.enable_or_disable('strict'))
        return args
