"""test_utils.py: Utilities for unit tests."""

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


import os
import pandas as pd


DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'testdata')


def get_test_filepath(fn):
    test_fp = os.path.join(DATA_DIR, fn)
    assert os.path.exists(test_fp)
    return(test_fp)


def load_test_file_as_text(fp):
    with open(fp, 'r') as file:
        file_contents=file.read()
    return(file_contents)


def load_test_dataframe(fp):
    return(pd.read_pickle(fp))


def get_test_data(prefix):

    input_fp = get_test_filepath(prefix + '_ua_dg.hyb')
    input_data = load_test_file_as_text(input_fp)

    test_fp = get_test_filepath(prefix + '_ua_dg.summarise_hyb_file.tab')
    test_data = load_test_file_as_text(test_fp)

    input_hyb_pkl_fp = get_test_filepath(prefix + '_ua_dg.hyb_df.pkl')
    input_hyb_pkl = load_test_dataframe(input_hyb_pkl_fp)

    return input_fp, input_data, test_fp, test_data, input_hyb_pkl_fp, input_hyb_pkl
