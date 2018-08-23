"""Summarise a hyb dataframe."""

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


import pandas as pd

from hybtools.constants import SummaryLevel


def extract_description_elements(hyb_df, element_index):
    """Extract the elements from a description field.

    Given a hyb DataFrame as input, return a hyb dataframe with each description column replaced by the nth element
    within the original description column, where n is the zero based element_index.

    :param hyb_df: A pandas DataFrame representing a hyb file.
    :type hyb_df: pd.DataFrame
    :param element_index: The index of the element of each description column to extract.
    :type element_index: int

    :returns: A pandas DataFrame identical to the input DataFrame, except that each description column has been replaced
        by the element at the specified index.

    """
    for description in ['bit1-description', 'bit2-description']:
        hyb_df[description] = hyb_df[description].map(lambda x: x.strip().split('_')[element_index])
    return hyb_df


def create_summary_dataframe(hyb_df, level=SummaryLevel.DESCRIPTION, cutoff=0, non_directional=False, by_fragment=False):
    """Create a summary DataFrame.

    :param hyb_df: A pandas DataFrame representing a hyb file.
    :type hyb_df: pd.DataFrame
    :param level: The level at which the hyb DataFrame should be summarised.
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
    # Modify the hyb dataframe to reflect the summary level given as input
    if level == SummaryLevel.ID:
        hyb_df = extract_description_elements(hyb_df, element_index=0)
    elif level == SummaryLevel.NAME:
        hyb_df = extract_description_elements(hyb_df, element_index=2)
    elif level == SummaryLevel.BIOTYPE:
        hyb_df = extract_description_elements(hyb_df, element_index=3)
    else:
        pass  # assuming that the level is description

    # Generate the query dataframe, reflecting the information to be summarised
    if by_fragment:

        query_column = 'bit-description'
        count_column = 'fragment-count'

        bit_descriptions = hyb_df[['bit1-description', 'bit2-description']].values.flatten()
        query_df = pd.DataFrame({query_column: bit_descriptions})

    else:

        query_column = 'hybrid-description'
        count_column = 'hybrid-count'

        if non_directional:

            def get_sorted_hybrid_description(row):
                bits = [row['bit1-description'], row['bit2-description']]
                return ':::'.join(sorted(bits, reverse=True))

            hyb_df[query_column] = hyb_df.apply(get_sorted_hybrid_description, axis=1)

        else:

            hyb_df[query_column] = hyb_df['bit1-description'].str.cat(hyb_df['bit2-description'], sep=':::')

        query_df = hyb_df.loc[:, [query_column]]

    # Aggregate the values in the query dataframe
    summary_df = query_df[[query_column]].groupby(query_df[query_column]).count()

    # Sort the aggregated values
    summary_df.columns = [count_column]
    summary_df.sort_values(by=count_column, ascending=False, inplace=True)
    summary_df.reset_index([0], inplace=True)

    # Apply the cutoff and create the 'other' category
    if cutoff > 0:

        summary_df['cutoff-class'] = summary_df.apply(
            lambda row: row[query_column] if int(row[count_column]) > cutoff else 'other', axis=1
        )
        grouped = summary_df.groupby('cutoff-class')
        summary_df = grouped.sum()
        summary_df.reset_index([0], inplace=True)
        summary_df['is-other'] = summary_df['cutoff-class'].map(lambda x: 0 if x == 'other' else 1)
        summary_df.sort_values(by=['is-other', count_column], ascending=False, inplace=True)
        del summary_df['is-other']

    return summary_df
