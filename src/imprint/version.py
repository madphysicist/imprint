# -*- coding: utf-8 -*-

# imprint: a program for creating documents from data and content templates
#
# Copyright (C) 2019  Joseph R. Fox-Rabinovitz <jfoxrabinovitz at gmail dot com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Author: Joseph Fox-Rabinovitz <jfoxrabinovitz at gmail dot com>
# Version: 13 Apr 2019: Initial Coding
# Version: 20 Jan 2022: Bumped version to 0.1.0a2rc1

"""
:py:mod:`imprint.version` holds the version of the package.

The actual version number is normally exported through the top-level
:py:mod:`imprint` package, but defined here. This module exists to
facilitate deployment and testing, so users do not need to install the
entire package to get the version number.

Bump the version in the dev branch every time a prior version is tagged
in master. Unless a major rewrite is planned, the new version should
increment the minor number. The new version should be a release
candidate, and have the corresponding `rc1` suffix. All following
commits belong to the new version. Bump to full version immediately
before merging with master. A tag is assigned on the master commit that
merges in dev. Bump the version in dev immediately after merging master
back in.
"""

#: The current version
__version__ = '0.1.0a2'
