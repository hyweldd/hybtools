"""cli.py: Command line entry point module for the hybtools package."""

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
import sys

from hybtools import commands


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
FULL_FILEPATH = click.Path(exists=True, dir_okay=False, allow_dash=True, readable=True, resolve_path=True)


def write_tsv(df):
    df.to_csv(sys.stdout, sep = '\t', header = False, index = False)


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass


@main.command()
@click.argument('hyb_filepath', type=FULL_FILEPATH, default='-')
def summarise(hyb_filepath):
    """Summarise hybrids in a hyb file."""
    commands.summarise(hyb_filepath=hyb_filepath).pipe(write_tsv)



