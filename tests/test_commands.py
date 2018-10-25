"""Test the commands module."""

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


from hybtools import commands, summarise, hybfilter
from tests.testutils import get_test_filepath, load_test_dataframe


class TestSummarise(object):
    """Tests for the summarise command."""

    # Helper method
    @staticmethod
    def run_summarise_test(input_fn, test_fn, **kwargs):
        """Helper method to run summarise tests with different parameters."""

        input_fp = get_test_filepath(input_fn)
        test_df = load_test_dataframe(test_fn, data_dir_suffix='summarise')

        result = commands.summarise(hyb_filepath=input_fp, **kwargs)

        assert result.equals(test_df)

    # Test methods
    @staticmethod
    def test_summarise_with_default_parameters():

        TestSummarise.run_summarise_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summary_description_directional_c0_hyb_df.pkl.gz'
        )

    @staticmethod
    def test_summarise_description_directional_c0():

        TestSummarise.run_summarise_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summary_description_directional_c0_hyb_df.pkl.gz',
            level=summarise.SummaryLevel.DESCRIPTION,
            cutoff=0,
            non_directional=False,
            by_fragment=False
        )

    @staticmethod
    def test_summarise_name_directional_c0():

        TestSummarise.run_summarise_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summary_name_directional_c0_hyb_df.pkl.gz',
            level=summarise.SummaryLevel.NAME,
            cutoff=0,
            non_directional=False,
            by_fragment=False
        )

    @staticmethod
    def test_summarise_id_directional_c0():

        TestSummarise.run_summarise_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summary_id_directional_c0_hyb_df.pkl.gz',
            level=summarise.SummaryLevel.ID,
            cutoff=0,
            non_directional=False,
            by_fragment=False
        )

    @staticmethod
    def test_summarise_biotype_directional_c0():

        TestSummarise.run_summarise_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summary_biotype_directional_c0_hyb_df.pkl.gz',
            level=summarise.SummaryLevel.BIOTYPE,
            cutoff=0,
            non_directional=False,
            by_fragment=False
        )

    @staticmethod
    def test_summarise_description_nondirectional_c0():

        TestSummarise.run_summarise_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summary_description_nondirectional_c0_hyb_df.pkl.gz',
            level=summarise.SummaryLevel.DESCRIPTION,
            cutoff=0,
            non_directional=True,
            by_fragment=False
        )

    @staticmethod
    def test_summarise_description_nondirectional_c5():

        TestSummarise.run_summarise_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summary_description_nondirectional_c5_hyb_df.pkl.gz',
            level=summarise.SummaryLevel.DESCRIPTION,
            cutoff=5,
            non_directional=True,
            by_fragment=False
        )

    @staticmethod
    def test_summarise_description_byfragment_c0():

        TestSummarise.run_summarise_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summary_description_byfragment_c0_hyb_df.pkl.gz',
            level=summarise.SummaryLevel.DESCRIPTION,
            cutoff=0,
            non_directional=True,
            by_fragment=True
        )

    @staticmethod
    def test_summarise_description_byfragment_c5():

        TestSummarise.run_summarise_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summary_description_byfragment_c5_hyb_df.pkl.gz',
            level=summarise.SummaryLevel.DESCRIPTION,
            cutoff=5,
            non_directional=True,
            by_fragment=True
        )


class TestFilterHyb(object):
    """Tests for the filter_hyb command."""

    # Helper method
    @staticmethod
    def run_filter_hyb_test(input_fn, test_fn, data_dir_suffix='filter', **kwargs):
        """Helper function to run filter tests with different parameters."""

        input_fp = get_test_filepath(input_fn)
        test_df = load_test_dataframe(test_fn, data_dir_suffix=data_dir_suffix)

        result = commands.filter_hyb(hyb_filepath=input_fp, **kwargs)
        assert result.equals(test_df)

    # Test methods
    @staticmethod
    def test_filter_hyb_with_default_parameters():
        """Running filter_hyb with default parameters should return the unfiltered hyb DataFrame."""

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.hyb_df.pkl.gz',
            data_dir_suffix=''
        )

    @staticmethod
    def test_filter_hyb_intermolecular():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_intermolecular_hyb_df.pkl.gz',
            hybrid_type=hybfilter.HybridType.INTERMOLECULAR
        )

    @staticmethod
    def test_filter_hyb_intramolecular():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_intramolecular_hyb_df.pkl.gz',
            hybrid_type=hybfilter.HybridType.INTRAMOLECULAR
        )

    @staticmethod
    def test_filter_hyb_all():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_all_hyb_df.pkl.gz',
            hybrid_type=hybfilter.HybridType.ALL
        )

    @staticmethod
    def test_filter_hyb_dgminus10():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_all_dgminus10_hyb_df.pkl.gz',
            hybrid_type=hybfilter.HybridType.ALL,
            dg=-10
        )

    @staticmethod
    def test_filter_hyb_dgminus10_invert():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_all_dgminus10_invert_hyb_df.pkl.gz',
            hybrid_type=hybfilter.HybridType.ALL,
            dg=-10,
            invert=True
        )

    @staticmethod
    def test_filter_hyb_pre47S_SNORD68_nn():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_pre47S_SNORD68_nn_hyb_df.pkl.gz',
            description_filter='pre47S:::SNORD68',
            description_element_types='nn'
        )

    @staticmethod
    def test_filter_hyb_pre47S_SNORD68_nn_directional():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_pre47S_SNORD68_nn_directional_hyb_df.pkl.gz',
            description_filter='pre47S:::SNORD68',
            description_element_types='nn',
            directional=True
        )

    @staticmethod
    def test_filter_hyb_SNORD68_pre47S_nn():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S',
            description_element_types='nn'
        )

    @staticmethod
    def test_filter_hyb_SNORD68_pre47S_directional_nn():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_nn_directional_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S',
            description_element_types='nn',
            directional=True
        )

    @staticmethod
    def test_filter_hyb_SNORD68_pre47S_3700_3800_nn():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_3700_3800_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S(3700-3800)',
            description_element_types='nn',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_SNORD68_pre47S_3750_nn():
        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_3750_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S(3750)',
            description_element_types='nn',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_SNORD68_pre47S_3750_lenient_nn():
        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_3750_lenient_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S(3750)',
            description_element_types='nn',
            directional=False,
            lenient=True
        )

    @staticmethod
    def test_filter_hyb_SNORD68_pre47S_3740_3750_nn():
        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_3740_3750_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S(3740-3750)',
            description_element_types='nn',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_SNORD68_pre47S_3740_3750_lenient_nn():
        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_pre47S_3740_3750_lenient_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::pre47S(3740-3750)',
            description_element_types='nn',
            directional=False,
            lenient=True
        )

    @staticmethod
    def test_filter_hyb_SNORD68_10_50_pre47S_nn():
        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_10_50_pre47S_nn_hyb_df.pkl.gz',
            description_filter='SNORD68(10-50):::pre47S',
            description_element_types='nn',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_SNORD68_10_50_pre47S_lenient_nn():
        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_10_50_pre47S_lenient_nn_hyb_df.pkl.gz',
            description_filter='SNORD68(10-50):::pre47S',
            description_element_types='nn',
            directional=False,
            lenient=True
        )

    @staticmethod
    def test_filter_hyb_rRNA_SNORD68_nn():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_rRNA_SNORD68_nn_hyb_df.pkl.gz',
            description_filter='rRNA:::SNORD68',
            description_element_types='bn'
        )

    @staticmethod
    def test_filter_hyb_rRNA_SNORD68_nn_directional():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_rRNA_SNORD68_nn_directional_hyb_df.pkl.gz',
            description_filter='rRNA:::SNORD68',
            description_element_types='bn',
            directional=True
        )

    @staticmethod
    def test_filter_hyb_SNORD68_rRNA_nn():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA',
            description_element_types='nb'
        )

    @staticmethod
    def test_filter_hyb_SNORD68_rRNA_directional_nn():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_nn_directional_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA',
            description_element_types='nb',
            directional=True
        )

    @staticmethod
    def test_filter_hyb_SNORD68_rRNA_3700_3800_nn():

        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_3700_3800_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA(3700-3800)',
            description_element_types='nb',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_SNORD68_rRNA_3750_nn():
        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_3750_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA(3750)',
            description_element_types='nb',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_SNORD68_rRNA_3750_lenient_nn():
        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_3750_lenient_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA(3750)',
            description_element_types='nb',
            directional=False,
            lenient=True
        )

    @staticmethod
    def test_filter_hyb_SNORD68_rRNA_3740_3750_nn():
        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_3740_3750_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA(3740-3750)',
            description_element_types='nb',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_SNORD68_rRNA_3740_3750_lenient_nn():
        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_rRNA_3740_3750_lenient_nn_hyb_df.pkl.gz',
            description_filter='SNORD68:::rRNA(3740-3750)',
            description_element_types='nb',
            directional=False,
            lenient=True
        )

    @staticmethod
    def test_filter_hyb_SNORD68_10_50_rRNA_nn():
        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_10_50_rRNA_nn_hyb_df.pkl.gz',
            description_filter='SNORD68(10-50):::rRNA',
            description_element_types='nb',
            directional=False
        )

    @staticmethod
    def test_filter_hyb_SNORD68_10_50_rRNA_lenient_nn():
        TestFilterHyb.run_filter_hyb_test(
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.filtered_SNORD68_10_50_rRNA_lenient_nn_hyb_df.pkl.gz',
            description_filter='SNORD68(10-50):::rRNA',
            description_element_types='nb',
            directional=False,
            lenient=True
        )
