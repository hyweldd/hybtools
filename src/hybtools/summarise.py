"""summarise.py: Functions for summarising a hyb dataframe."""

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


def create_summary_dataframe(hyb_df):
    """Create a summary dataframe given a hyb dataframe as input."""

    hyb_df['hybrid-description'] = hyb_df['bit1-description'].str.cat(hyb_df['bit2-description'], sep =':::')

    query_column = 'hybrid-description'

    summary_df = hyb_df[[query_column]].groupby(hyb_df[query_column]).count()

    summary_df.columns = ['hybrid-count']
    summary_df.sort_values(by='hybrid-count', ascending=False, inplace=True)
    summary_df.reset_index(0, inplace=True)

    return(summary_df)



