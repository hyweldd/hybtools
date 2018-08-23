"""Provide a high level python interface for the hybtools package."""

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


from hybtools.io import load_hyb_dataframe
from hybtools.summarise import create_summary_dataframe
from hybtools.constants import SummaryLevel


def summarise(hyb_filepath, level=SummaryLevel.DESCRIPTION, cutoff=0, non_directional=False, by_fragment=False):
    """Summarise a hyb file.

    :param hyb_filepath: The path to the input hyb file, or "-" to represent standard input.
    :type hyb_filepath: str
    :param level: The level at which the hyb file should be summarised.
    :type level: SummaryLevel
    :param cutoff: The minimum value for which a separate row is included. Rows with values below this cutoff are
            aggregated into a category named "other".
    :type cutoff: int
    :param non_directional: A flag specifying whether to aggregate hybrids involving the same elements
            in a different order.
    :type non_directional: bool
    :param by_fragment: A flag specifying whether to summarise by hybrid fragments rather than hybrids.
    :type by_fragment: bool

    :returns: A summary of the hyb file at the given file path as a pandas dataframe.

    """
    hyb_df = load_hyb_dataframe(hyb_filepath)

    summary_hyb_df = create_summary_dataframe(
        hyb_df=hyb_df,
        level=level,
        cutoff=cutoff,
        non_directional=non_directional,
        by_fragment=by_fragment
    )

    return summary_hyb_df
