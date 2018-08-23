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


from hybtools import commands, summarise
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
