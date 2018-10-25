"""Test the filter module."""

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


from hybtools import hybfilter
from tests.testutils import load_test_dataframe


# def filter_hyb_dataframe(
#     hyb_df,
#     hybrid_type=HybridType.ALL,
#     dg=None,
#     description_filter=None,
#     description_element_types=None,
#     lenient=False,
#     directional=False,
#     invert=False
# ):

class TestFilterHybDataFrame(object):
    """Tests for the filter_hyb_dataframe function."""

    # Helper method
    @staticmethod
    def run_filter_hyb_dataframe_test(input_fn, test_fn, data_dir_suffix='filter', **kwargs):
        """Helper function to run filter_hyb_dataframe tests with different parameters."""

        input_df = load_test_dataframe(input_fn)
        test_df = load_test_dataframe(test_fn, data_dir_suffix=data_dir_suffix)

        result = hybfilter.filter_hyb_dataframe(hyb_df=input_df, **kwargs)
        assert result.equals(test_df)

    # Test methods
    @staticmethod
    def test_filter_hyb_dataframe_with_default_parameters():
        """Running filter_hyb_dataframe with default parameters should return the unfiltered hyb DataFrame."""

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.hyb_df.pkl.gz',
            data_dir_suffix=''
        )

    @staticmethod
    def test_filter_hyb_dataframe_intermolecular():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_intermolecular_hyb_df.pkl.gz',
            hybrid_type=hybfilter.HybridType.INTERMOLECULAR
        )

    @staticmethod
    def test_filter_hyb_dataframe_intramolecular():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_intramolecular_hyb_df.pkl.gz',
            hybrid_type=hybfilter.HybridType.INTRAMOLECULAR
        )

    @staticmethod
    def test_filter_hyb_dataframe_all():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_all_hyb_df.pkl.gz',
            hybrid_type=hybfilter.HybridType.ALL
        )

    @staticmethod
    def test_filter_hyb_dataframe_dgminus10():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_all_dgminus10_hyb_df.pkl.gz',
            hybrid_type=hybfilter.HybridType.ALL,
            dg=-10
        )

    @staticmethod
    def test_filter_hyb_dataframe_dgminus10_invert():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_all_dgminus10_invert_hyb_df.pkl.gz',
            hybrid_type=hybfilter.HybridType.ALL,
            dg=-10,
            invert=True
        )

    @staticmethod
    def test_filter_hyb_dataframe_pre47S_SNORD68_nn():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_pre47S_SNORD68_nn_hyb_df.pkl.gz',
            description_filter='pre47S:::SNORD68',
            description_element_types='nn'
        )

    @staticmethod
    def test_filter_hyb_dataframe_pre47S_SNORD68_nn_directional():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_pre47S_SNORD68_nn_directional_hyb_df.pkl.gz',
            description_filter='pre47S:::SNORD68',
            description_element_types='nn',
            directional=True
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_pre47S_nn():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S',
            description_element_types='nn'
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_pre47S_directional_nn():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_nn_directional_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S',
            description_element_types='nn',
            directional=True
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_pre47S_3700_3800_nn():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_3700_3800_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S(3700-3800)',
            description_element_types='nn',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_pre47S_3750_nn():
        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_3750_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S(3750)',
            description_element_types='nn',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_pre47S_3750_lenient_nn():
        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_3750_lenient_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S(3750)',
            description_element_types='nn',
            directional=False,
            lenient=True
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_pre47S_3740_3750_nn():
        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_3740_3750_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S(3740-3750)',
            description_element_types='nn',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_pre47S_3740_3750_lenient_nn():
        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_3740_3750_lenient_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S(3740-3750)',
            description_element_types='nn',
            directional=False,
            lenient=True
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_10_50_pre47S_nn():
        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_10_50_pre47S_nn_hyb_df.pkl.gz',
            description_filter='SNORD68(10-50):::pre47S',
            description_element_types='nn',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_10_50_pre47S_lenient_nn():
        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_10_50_pre47S_lenient_nn_hyb_df.pkl.gz',
            description_filter='SNORD68(10-50):::pre47S',
            description_element_types='nn',
            directional=False,
            lenient=True
        )

    @staticmethod
    def test_filter_hyb_dataframe_rRNA_SNORD68_nn():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_rRNA_SNORD68_nn_hyb_df.pkl.gz',
            description_filter='rRNA:::SNORD68',
            description_element_types='bn'
        )

    @staticmethod
    def test_filter_hyb_dataframe_rRNA_SNORD68_nn_directional():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_rRNA_SNORD68_nn_directional_hyb_df.pkl.gz',
            description_filter='rRNA:::SNORD68',
            description_element_types='bn',
            directional=True
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_rRNA_nn():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA',
            description_element_types='nb'
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_rRNA_directional_nn():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_nn_directional_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA',
            description_element_types='nb',
            directional=True
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_rRNA_3700_3800_nn():

        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_3700_3800_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA(3700-3800)',
            description_element_types='nb',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_rRNA_3750_nn():
        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_3750_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA(3750)',
            description_element_types='nb',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_rRNA_3750_lenient_nn():
        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_3750_lenient_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA(3750)',
            description_element_types='nb',
            directional=False,
            lenient=True
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_rRNA_3740_3750_nn():
        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_3740_3750_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA(3740-3750)',
            description_element_types='nb',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_rRNA_3740_3750_lenient_nn():
        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_3740_3750_lenient_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA(3740-3750)',
            description_element_types='nb',
            directional=False,
            lenient=True
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_10_50_rRNA_nn():
        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_10_50_rRNA_nn_hyb_df.pkl.gz',
            description_filter='SNORD68(10-50):::rRNA',
            description_element_types='nb',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_dataframe_SNORD68_10_50_rRNA_lenient_nn():
        TestFilterHybDataFrame.run_filter_hyb_dataframe_test(
            input_fn='test_ua_dg.hyb_df.pkl.gz',
            test_fn='test_ua_dg.filtered_SNORD68_10_50_rRNA_lenient_nn_hyb_df.pkl.gz',
            description_filter='SNORD68(10-50):::rRNA',
            description_element_types='nb',
            directional=False,
            lenient=True
        )
