#!/usr/bin/python
#
# CDDL HEADER START
#
# The contents of this file are subject to the terms of the
# Common Development and Distribution License (the "License").
# You may not use this file except in compliance with the License.
#
# You can obtain a copy of the license at usr/src/OPENSOLARIS.LICENSE
# or http://www.opensolaris.org/os/licensing.
# See the License for the specific language governing permissions
# and limitations under the License.
#
# When distributing Covered Code, include this CDDL HEADER in each
# file and include the License file at usr/src/OPENSOLARIS.LICENSE.
# If applicable, add the following below this CDDL HEADER, with the
# fields enclosed by brackets "[]" replaced with your own identifying
# information: Portions Copyright [yyyy] [name of copyright owner]
#
# CDDL HEADER END
#

# Copyright 2010 Sun Microsystems, Inc.  All rights reserved.
# Use is subject to license terms.

import testutils
if __name__ == "__main__":
        testutils.setup_environment("../../../proto")
import pkg5unittest

import unittest
import os

class TestPkgRebuildIndex(pkg5unittest.SingleDepotTestCase):
        # Only start/stop the depot once (instead of for every test)
        persistent_setup = True

        def test_rebuild_index_bad_opts(self):
                """Test pkg with bad options."""

		durl = self.dc.get_depot_url()
                self.image_create(durl)

                self.pkg("rebuild-index -@", exit=2)
                self.pkg("rebuild-index foo", exit=2)
                self.pkg("rebuild-index --", exit=2)

        def test_rebuild_index_bad_perms(self):
                """Testing for bug 4570."""

		durl = self.dc.get_depot_url()
                self.image_create(durl)
                self.pkg("rebuild-index")
                self.pkg("rebuild-index", exit=1, su_wrap=True)


if __name__ == "__main__":
        unittest.main()
