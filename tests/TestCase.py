# Copyright (C) 2016 Adam Schubert <adam.schubert@sg1-game.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import unittest
import locale

__author__ = "Adam Schubert <adam.schubert@sg1-game.net>"
__date__ = "$2016-01-17 14:51:02$"


class TestCase(unittest.TestCase):

    """
    Test case for all tests
    """

    def setUp(self):
        """Set up en_US.utf8 locale
        """
        # all tests are written in en_US
        locale.setlocale(locale.LC_ALL, 'en_US.utf8')
