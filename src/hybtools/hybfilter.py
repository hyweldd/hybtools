"""Filter a hyb DataFrame."""

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


import collections
import pandas as pd


from hybtools.filterutils import DescriptionFilter
from hybtools.constants import HybridType


HybRecord = collections.namedtuple(
    'HybRecord',
    'unique_sequence_id   read_sequence   predicted_binding_energy   '
    'bit1_description   bit1_read_coordinates_start   bit1_read_coordinates_stop   bit1_transcript_coordinates_start   '
    'bit1_transcript_coordinates_stop   bit1_mapping_score   '
    'bit2_description   bit2_read_coordinates_start   bit2_read_coordinates_stop   bit2_transcript_coordinates_start   '
    'bit2_transcript_coordinates_stop   bit2_mapping_score   '
    'annotations'
)


def HybRecord_from_line(hyb_line):
    hyb_line_elements = hyb_line.strip().split('\t')
    core_line_elements = hyb_line_elements[:15]
    annotations = ['\t'.join(hyb_line_elements[15:])] if len(hyb_line_elements) > 15 else ['']
    return HybRecord(*(core_line_elements + annotations))


def filter_hyb_dataframe(
    hyb_df,
    hybrid_type=HybridType.ALL,
    dg=None,
    description_filter=None,
    description_element_types=None,
    lenient=False,
    directional=False,
    invert=False
):
    """Filter a hyb DataFrame.

    Given a hyb DataFrame as input, remove the rows matching the filters and flags specified in
    the input parameters and return the resulting DataFrame.

    :param hyb_df: A pandas DataFrame representing a hyb file.
    :type hyb_df: pd.DataFrame
    :param hybrid_type: The type of hybrid to retain. Unless the invert flag is set all rows representing hybrids
            that are not of the specified type are removed. Passing a hybrid type of ALL results in no hybrid types
            being excluded.
    :type hybrid_type: HybridType
    :param dg: The threshold dG value. Unless the invert flag is set all rows with a dG value above this threshold
            are removed.
    :type dg: int
    :param description_filter: A string representing a filtering criterion to be applied to the hyb DataFrame.
    :type description_filter: str
    :param description_element_types: A string describing the element types used in the description filter.
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

    def update_exclusions(df, new_exclusions):
        """Update the exclude column in the hyb DataFrame."""
        df['exclude'] = (df['exclude'] | new_exclusions)
        return df

    hyb_df['exclude'] = False

    # Add exclusions based on hybrid type
    if hybrid_type == HybridType.INTERMOLECULAR:
        hyb_df = update_exclusions(hyb_df, hyb_df['bit1-description'] == hyb_df['bit2-description'])
    elif hybrid_type == HybridType.INTRAMOLECULAR:
        hyb_df = update_exclusions(hyb_df, hyb_df['bit1-description'] != hyb_df['bit2-description'])

    # Add exclusions based on dG
    if dg is not None:
        hyb_df = update_exclusions(hyb_df, hyb_df['predicted_binding_energy'].astype(float, copy=True) > dg)

    # Add exclusions based on description filter
    if description_filter is not None and description_element_types is not None:

        desc_filter = DescriptionFilter(
            description_filter=description_filter,
            description_element_type=description_element_types,
            lenient=lenient
        )

        # TODO - refactor this to be more efficient using apply
        should_exclude = []

        for hyb_record_string in \
                hyb_df.to_string(header=False, index=False, index_names=False, na_rep='').split('\n'):

            cleaned_hyb_record_string = '\t'.join(list(filter(None, hyb_record_string.split(' '))))
            hyb_record = HybRecord_from_line(cleaned_hyb_record_string)
            should_exclude.append(
                desc_filter.should_exclude_hyb_record(hyb_record=hyb_record, directional=directional)
            )

        hyb_df = hyb_df.assign(exclude=pd.Series(should_exclude, index=hyb_df.index))

    # Filter hyb DataFrame according to the exclusions
    hyb_df = hyb_df[hyb_df['exclude'] == invert]
    del hyb_df['exclude']

    return hyb_df
