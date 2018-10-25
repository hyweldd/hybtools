"""Test the command line interface."""

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


import click.testing
import pytest
from tests.testutils import get_test_filepath, load_file_contents_as_text


@pytest.fixture
def cli_runner(request):
    """Import the click test runner so that it can be used by pytest"""
    return click.testing.CliRunner()


def invoke_subcommand(
        cli_runner,
        subcommand,
        input_filepath,
        input_data=None,
        flags=()
):
    """Helper function to test a subcommand with input from either stdin or a file"""
    from hybtools.cli import main

    subcommand_with_flags = [subcommand]
    subcommand_with_flags.extend(flags)

    if input_filepath == '-':
        subcommand_with_flags.append('-')
        result = cli_runner.invoke(main, subcommand_with_flags, input=input_data)
    else:
        subcommand_with_flags.append(input_filepath)
        with cli_runner.isolated_filesystem():
            with open(input_filepath, 'w') as f:
                f.write(input_data)
            result = cli_runner.invoke(main, subcommand_with_flags)

    return result


def test_main(cli_runner):
    """Test the effect of running hybtools on its own. Should show the usage message."""
    from hybtools.cli import main
    result = cli_runner.invoke(main, [])
    assert result.exit_code == 0
    assert result.output.startswith('Usage')


def run_cli_test(subcommand, input_fn, test_fn, cli_runner, use_stdin, data_dir_suffix=None, flags=()):
    """Helper method to run cli tests with different parameters."""

    if data_dir_suffix is None:
        data_dir_suffix = subcommand

    input_fp = get_test_filepath(input_fn)
    input_data = load_file_contents_as_text(input_fp)

    test_fp = get_test_filepath(test_fn, data_dir_suffix=data_dir_suffix)
    test_data = load_file_contents_as_text(test_fp)

    result = invoke_subcommand(
        cli_runner=cli_runner,
        subcommand=subcommand,
        input_filepath='-' if use_stdin else input_fp,
        input_data=input_data,
        flags=flags
    )

    assert result.exit_code == 0
    assert result.output.rstrip() == test_data.rstrip()


class TestSummarise(object):
    """Tests for the summarise command with various options"""

    @staticmethod
    def test_summarise_file(cli_runner):
        """Test the effect of running the summarise command with a hyb file path given as input."""

        run_cli_test(
            subcommand='summarise',
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summarise_hyb_file.tab',
            cli_runner=cli_runner,
            use_stdin=False
        )

    @staticmethod
    def test_summarise_stdin(cli_runner):
        """Test the effect of running the summarise command with input passed to stdin."""

        run_cli_test(
            subcommand='summarise',
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summarise_hyb_file.tab',
            cli_runner=cli_runner,
            use_stdin=True
        )

    @staticmethod
    def test_summarise_file_nondirectional(cli_runner):
        """Test the effect of running the summarise command
        with a hyb file path given as input and the -n flag set."""

        run_cli_test(
            subcommand='summarise',
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summarise_hyb_file.non-directional.tab',
            cli_runner=cli_runner,
            use_stdin=False,
            flags=['-n']
        )

    @staticmethod
    def test_summarise_file_byfragment(cli_runner):
        """Test the effect of running the summarise command
        with a hyb file path given as input and the -f flag set."""

        run_cli_test(
            subcommand='summarise',
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summarise_hyb_file.by-fragment.tab',
            cli_runner=cli_runner,
            use_stdin=False,
            flags=['-f']
        )

    @staticmethod
    def test_summarise_file_cutoff_5(cli_runner):
        """Test the effect of running the summarise command
        with a hyb file path given as input and the cutoff set to 5."""

        run_cli_test(
            subcommand='summarise',
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summarise_hyb_file.cutoff_5.tab',
            cli_runner=cli_runner,
            use_stdin=False,
            flags=['-c', '5']
        )

    @staticmethod
    def test_summarise_file_level_id(cli_runner):
        """Test the effect of running the summarise command
        with a hyb file path given as input and the level set to id."""

        run_cli_test(
            subcommand='summarise',
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summarise_hyb_file.level_id.tab',
            cli_runner=cli_runner,
            use_stdin=False,
            flags=['-l', 'id']
        )

    @staticmethod
    def test_summarise_file_level_biotype(cli_runner):
        """Test the effect of running the summarise command
        with a hyb file path given as input and the level set to biotype."""

        run_cli_test(
            subcommand='summarise',
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.summarise_hyb_file.level_biotype.tab',
            cli_runner=cli_runner,
            use_stdin=False,
            flags=['-l', 'biotype']
        )


class TestFilter(object):
    """Tests for the filter command with various options"""

    @staticmethod
    def test_filter_file(cli_runner):
        """Test the effect of running the filter command with a hyb file path given as input, should return all rows."""

        run_cli_test(
            subcommand='filter',
            input_fn='test_ua_dg.hyb',
            test_fn='test_ua_dg.hyb',
            cli_runner=cli_runner,
            use_stdin=False,
            data_dir_suffix=''
        )
