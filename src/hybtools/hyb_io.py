"""hyb_io.py: hyb file I/O operations."""

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
import sys


hyb_df_columns = ['unique_sequence_id', 'read_sequence', 'predicted_binding_energy', 'bit1-description',
              'bit1-read_coordinates_start', 'bit1-read_coordinates_stop', 'bit1-transcript_coordinates_start',
              'bit1-transcript_coordinates_stop', 'bit1-mapping_score', 'bit2-description',
              'bit2-read_coordinates_start', 'bit2-read_coordinates_stop', 'bit2-transcript_coordinates_start',
              'bit2-transcript_coordinates_stop', 'bit2-mapping_score', 'annotations', 'comment']


def load_hyb_dataframe(hyb_filepath):
    """Import a hyb file as a dataframe."""

    if(hyb_filepath == "-"):
        hyb_filepath = sys.stdin

    hyb_df = pd.read_csv(hyb_filepath, sep = '\t', header = None, comment = '#', skip_blank_lines=True)

    assert 15 <= len(hyb_df.columns) <= 17, \
        "Input hyb file must have between 15 and 17 columns. This file has %d columns" % len(hyb_df.columns)

    hyb_df.columns = hyb_df_columns[0:len(hyb_df.columns)]

    return(hyb_df)
