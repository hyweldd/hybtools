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
from hybtools.hybfilter import filter_hyb_dataframe, HybridType


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


def filter_hyb(
        hyb_filepath,
        hybrid_type=HybridType.ALL,
        dg=None,
        invert=False,
        description_filter=None,
        description_element_types=None,
        lenient=False,
        directional=False
):
    """Filter a hyb file.

    :param hyb_filepath: The path to the input hyb file, or "-" to represent standard input.
    :type hyb_filepath: str
    :param hybrid_type: The type of hybrid to retain. Unless the invert flag is set all rows representing hybrids
            that are not of the specified type are removed. Passing a hybrid type of ALL results in no hybrid types
            being excluded.
    :type hybrid_type: HybridType
    :param dg: The threshold dG value. Unless the invert flag is set all rows with a dG value above this threshold
            are removed.
    :type dg: int
    :param description_filter: A string representing a filtering criterion to be applied to the hyb DataFrame.
    :type description_filter: str
    :param description_element_types: A string describing the types of the elements in the description filter.
    :type description_element_types: str
    :param lenient: A flag to indicate that the application of the description filters should be applied leniently.
    :type lenient: bool
    :param directional: TODO
    :type directional: bool
    :param invert: A flag to indicate that all rows that would be removed based on the preceding filters should be
            retained, and all rows that would be retained based on the preceding filters should be removed.

    :returns: A pandas DataFrame identical to the input DataFrame, except that the rows matching the filters and
            flags specified in the input parameters have been removed.

    """
    hyb_df = load_hyb_dataframe(hyb_filepath)

    filtered_df = filter_hyb_dataframe(
        hyb_df,
        hybrid_type=hybrid_type,
        dg=dg,
        description_filter=description_filter,
        description_element_types=description_element_types,
        lenient=lenient,
        directional=directional,
        invert=invert
    )

    return filtered_df
