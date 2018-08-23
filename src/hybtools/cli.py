"""Provide a command line entry point for the hybtools package."""

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


import click

from hybtools import __about__
from hybtools import commands


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
FULL_FILEPATH = click.Path(exists=True, dir_okay=False, allow_dash=True, readable=True, resolve_path=True)


def write_tsv(df):
    """Helper function to write a dataframe to stdout as a tsv file."""
    tsv = df.to_csv(sep='\t', header=False, index=False).rstrip()
    click.echo(tsv)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__about__.__version__)
def main():
    """A suite of command line tools for working with hyb and viennad files."""
    pass


@main.command()
@click.argument('hyb_filepath', type=FULL_FILEPATH, default='-')
@click.option('-l', '--level',
              help='The level at which aggregation occurs. '
                   'Default is description. Can also choose name, id, and biotype.',
              default='description')
@click.option('-c', '--cutoff',
              help='The minimum value for which a separate row should be shown in the output. '
                   'Rows with values below this cutoff will be aggregated into a category named "other". '
                   'Default is zero, meaning that separate rows are shown for all values.',
              default=0,
              type=int)
@click.option('-n', '--non-directional', is_flag=True,
              help='Do not aggregate hybrids involving the same elements in a different order.')
@click.option('-f', '--by-fragment', is_flag=True,
              help='Summarise by hybrid fragments rather than hybrids.')
def summarise(hyb_filepath, level, cutoff, non_directional, by_fragment):
    """Summarise hybrids in a hyb file."""
    from hybtools.summarise import SummaryLevel

    if level.lower() == 'description':
        summary_level = SummaryLevel.DESCRIPTION
    elif level.lower() == 'biotype':
        summary_level = SummaryLevel.BIOTYPE
    elif level.lower() == 'id':
        summary_level = SummaryLevel.ID
    else:
        summary_level = SummaryLevel.NAME

    commands.summarise(
        hyb_filepath=hyb_filepath,
        level=summary_level,
        cutoff=cutoff,
        non_directional=non_directional,
        by_fragment=by_fragment
    ).pipe(write_tsv)
