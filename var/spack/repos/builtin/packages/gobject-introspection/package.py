##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class GobjectIntrospection(Package):
    """The GObject Introspection is used to describe the program APIs and
    collect them in a uniform, machine readable format.Cairo is a 2D graphics
    library with support for multiple output"""

    homepage = "https://wiki.gnome.org/Projects/GObjectIntrospection"
    url      = "http://ftp.gnome.org/pub/gnome/sources/gobject-introspection/1.49/gobject-introspection-1.49.2.tar.xz"

    version('1.49.2', 'c47a76b05b2d8438089f519922180747')
    version('1.48.0', '01301fa9019667d48e927353e08bc218')

    depends_on("glib@2.49.2:", when="@1.49.2:")
    # version 1.48.0 build fails with glib 2.49.4
    depends_on("glib@2.48.1", when="@1.48.0")
    depends_on("python")
    depends_on("cairo")
    depends_on("bison", type="build")
    depends_on("flex", type="build")

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        # we need to filter this file to avoid an overly long hashbang line
        filter_file('@PYTHON@', 'python',
                    'tools/g-ir-tool-template.in')
        make()
        make("install")
