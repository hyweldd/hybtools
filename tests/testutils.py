"""Provide simple utility functions for unit tests."""

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


def get_test_filepath(fn, data_dir_suffix=''):
    """Get the full path to a test file with a given name in the testdata directory."""
    test_fp = os.path.join(DATA_DIR, data_dir_suffix, fn)
    assert os.path.exists(test_fp)
    return test_fp


def load_file_contents_as_text(fp):
    """Return the contents of the specified file as text."""
    with open(fp, 'r') as file:
        file_contents = file.read()
    return file_contents


def load_test_file_contents(fn, data_dir_suffix=''):
    """Return the contents of a test file with a given name in the testdata directory."""
    test_fp = get_test_filepath(fn, data_dir_suffix=data_dir_suffix)
    return load_file_contents_as_text(test_fp)


def load_test_dataframe(fn, data_dir_suffix=''):
    """Return a dataframe that has been stored with a given name in the testdata directory in gzipped pickle format."""
    fp = get_test_filepath(fn, data_dir_suffix=data_dir_suffix)
    return pd.read_pickle(fp, compression='gzip')
