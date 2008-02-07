# browsershots.org - Test your web design in different browsers
# Copyright (C) 2007 Johann C. Rocholl <johann@browsershots.org>
#
# Browsershots is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Browsershots is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
Helper functions, with doctest.
"""

__revision__ = "$Rev$"
__date__ = "$Date$"
__author__ = "$Author$"


def remove_version_number(text):
    """
    Remove the version number from the end of a string.
    >>> remove_version_number('Firefox 3 Beta 2')
    'Firefox'
    >>> remove_version_number('Title - Netscape Navigator 9.0')
    'Title - Netscape Navigator'
    >>> remove_version_number(' Example 0.4-3556_4')
    ' Example'
    """
    while True:
        if text.lower().endswith('alpha'):
            text = text[:-5]
        elif text.lower().endswith('beta'):
            text = text[:-4]
        elif text[-1] in '0123456789.-_ ':
            text = text[:-1]
        else:
            return text


if __name__ == '__main__':
    import doctest
    doctest.testmod()
