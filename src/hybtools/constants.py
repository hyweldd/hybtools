"""Define application constants for the hybtools package."""

# ______________________________________________________________________________
#
#     hybtools
#     Copyright (C) 2017-2018  Hywel Dunn-Davies
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ______________________________________________________________________________


from aenum import Enum


class HybridType(Enum):
    """Enumerate the possible hybrid types.

    An Enum listing the different hybrid types that are recognised by the filter command.

    """

    ALL = 1
    INTERMOLECULAR = 2
    INTRAMOLECULAR = 3


class SummaryLevel(Enum):
    """Enumerate the possible summary levels.

    An Enum listing the different levels at which a hyb file can be summarised.

    """

    DESCRIPTION = 1
    ID = 2
    NAME = 3
    BIOTYPE = 4
