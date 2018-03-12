"""test_cli.py: Unit tests for the command line interface."""

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
from tests.testutils import get_test_filepath, load_test_file_as_text


@pytest.fixture
def cli_runner(request):
    '''Import the click test runner so that it can be used by pytest'''
    return click.testing.CliRunner()


def invoke_subcommand(
        subcommand,
        input_filename,
        cli_runner,
        input_file_contents = None,
        stdin_contents = None
    ):
    '''Helper function to test a subcommand with input from either stdin or a file'''
    from hybtools.cli import main

    if input_filename == '-':
        result = cli_runner.invoke(main, [subcommand, '-'], input = stdin_contents)
    else:
        with cli_runner.isolated_filesystem():
            with open(input_filename, 'w') as f:
                f.write(input_file_contents)
            result = cli_runner.invoke(main, [subcommand, input_filename])

    return result


def test_main(cli_runner):
    '''Test the effect of running hybtools on its own. Should show the usage message.'''
    from hybtools.cli import main
    result = cli_runner.invoke(main, [])
    assert result.exit_code == 0
    assert result.output.startswith('Usage')


def test_summarise_file(cli_runner):
    '''Test the effect of running the summarise command with a hyb file path given as input.'''

    input_fp = get_test_filepath('test_ua_dg.hyb')
    input_data = load_test_file_as_text(input_fp)

    test_fp = get_test_filepath('test_ua_dg.summarise_hyb_file.tab')
    test_data = load_test_file_as_text(test_fp)

    result = invoke_subcommand(
        subcommand = 'summarise',
        input_filename = input_fp,
        input_file_contents = input_data,
        cli_runner = cli_runner
    )
    assert result.exit_code == 0
    assert result.output.rstrip() == test_data.rstrip()


def test_summarise_stdin(cli_runner):
    '''Test the effect of running the summarise command with input passed to stdin.'''

    input_fp = get_test_filepath('test_ua_dg.hyb')
    input_data = load_test_file_as_text(input_fp)

    test_fp = get_test_filepath('test_ua_dg.summarise_hyb_file.tab')
    test_data = load_test_file_as_text(test_fp)

    result = invoke_subcommand(
        subcommand = 'summarise',
        input_filename = '-',
        stdin_contents = input_data,
        cli_runner = cli_runner
    )

    assert result.exit_code == 0
    assert result.output.rstrip() == test_data.rstrip()
