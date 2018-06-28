"""test_summarise.py: Unit tests for the summarise module."""

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


import pytest

from hybtools import summarise
from tests.testutils import get_test_filepath, load_test_dataframe


def test_create_summary_dataframe():
    '''Test the create_summary_dataframe function.'''

    input_fp = get_test_filepath('test_ua_dg.hyb_df.pkl.gz')
    test_fp = get_test_filepath('test_ua_dg.summary_hyb_df.pkl.gz')

    hyb_df = load_test_dataframe(input_fp)
    test_hyb_df = load_test_dataframe(test_fp)

    result = summarise.create_summary_dataframe(hyb_df = hyb_df)

    assert result.equals(test_hyb_df)


