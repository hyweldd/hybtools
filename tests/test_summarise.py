"""Test the summarise module."""

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


from hybtools import summarise
from hybtools.constants import SummaryLevel

from tests.testutils import load_test_dataframe


# Helper function
def run_create_summary_dataframe_test(input_fn, test_fn, **kwargs):
    """Helper function to run create_summary_dataframe tests with different parameters."""

    input_df = load_test_dataframe(input_fn)
    test_df = load_test_dataframe(test_fn, data_dir_suffix='summarise')

    result = summarise.create_summary_dataframe(hyb_df=input_df, **kwargs)

    assert result.equals(test_df)


# Test functions
def test_create_summary_dataframe_with_default_parameters():

    run_create_summary_dataframe_test(
        input_fn='test_ua_dg.hyb_df.pkl.gz',
        test_fn='test_ua_dg.summary_description_directional_c0_hyb_df.pkl.gz'
    )


def test_create_summary_dataframe_description_directional_c0():

    run_create_summary_dataframe_test(
        input_fn='test_ua_dg.hyb_df.pkl.gz',
        test_fn='test_ua_dg.summary_description_directional_c0_hyb_df.pkl.gz',
        level=SummaryLevel.DESCRIPTION,
        cutoff=0,
        non_directional=False,
        by_fragment=False
    )


def test_create_summary_dataframe_name_directional_c0():

    run_create_summary_dataframe_test(
        input_fn='test_ua_dg.hyb_df.pkl.gz',
        test_fn='test_ua_dg.summary_name_directional_c0_hyb_df.pkl.gz',
        level=SummaryLevel.NAME,
        cutoff=0,
        non_directional=False,
        by_fragment=False
    )


def test_create_summary_dataframe_id_directional_c0():

    run_create_summary_dataframe_test(
        input_fn='test_ua_dg.hyb_df.pkl.gz',
        test_fn='test_ua_dg.summary_id_directional_c0_hyb_df.pkl.gz',
        level=SummaryLevel.ID,
        cutoff=0,
        non_directional=False,
        by_fragment=False
    )


def test_create_summary_dataframe_biotype_directional_c0():

    run_create_summary_dataframe_test(
        input_fn='test_ua_dg.hyb_df.pkl.gz',
        test_fn='test_ua_dg.summary_biotype_directional_c0_hyb_df.pkl.gz',
        level=SummaryLevel.BIOTYPE,
        cutoff=0,
        non_directional=False,
        by_fragment=False
    )


def test_create_summary_dataframe_description_nondirectional_c0():

    run_create_summary_dataframe_test(
        input_fn='test_ua_dg.hyb_df.pkl.gz',
        test_fn='test_ua_dg.summary_description_nondirectional_c0_hyb_df.pkl.gz',
        level=SummaryLevel.DESCRIPTION,
        cutoff=0,
        non_directional=True,
        by_fragment=False
    )


def test_create_summary_dataframe_description_nondirectional_c5():

    run_create_summary_dataframe_test(
        input_fn='test_ua_dg.hyb_df.pkl.gz',
        test_fn='test_ua_dg.summary_description_nondirectional_c5_hyb_df.pkl.gz',
        level=SummaryLevel.DESCRIPTION,
        cutoff=5,
        non_directional=True,
        by_fragment=False
    )


def test_create_summary_dataframe_description_byfragment_c0():

    run_create_summary_dataframe_test(
        input_fn='test_ua_dg.hyb_df.pkl.gz',
        test_fn='test_ua_dg.summary_description_byfragment_c0_hyb_df.pkl.gz',
        level=SummaryLevel.DESCRIPTION,
        cutoff=0,
        non_directional=True,
        by_fragment=True
    )


def test_create_summary_dataframe_description_byfragment_c5():

    run_create_summary_dataframe_test(
        input_fn='test_ua_dg.hyb_df.pkl.gz',
        test_fn='test_ua_dg.summary_description_byfragment_c5_hyb_df.pkl.gz',
        level=SummaryLevel.DESCRIPTION,
        cutoff=5,
        non_directional=True,
        by_fragment=True
    )
