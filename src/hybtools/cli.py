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


@main.command()
@click.argument('input_filepath', type=FULL_FILEPATH, default='-')
@click.option('-t', '--type',
              help='The type of hybrid to filter by. '
                   'Possible values are all, intra (intramolecular), and inter (intermolecular). Default is all.',
              default='all')
@click.option('-g', '--deltaG',
              help='The delta G threshold to filter by. '
                   'All hybrids with delta G values below the specified threshold will be included.',
              type=float)
@click.option('-f', '--description_filter',
              # multiple=True,
              help='A description to filter by. A description is composed of two description elements separated by :::.'
                    # 'Multiple descriptions can be specified. In this case all lines that match any of the filters will be included.'
                    'If none are specified all hybrids will be included. You can also specify a co-ordinate range to '
                   'filter by on each side of the filter. For example snoRNA(1-50):::mRNA(100-125).'
                    'In addition, if the input file is a viennad file, you can specify the number of mismatches '
                   'to allow (in curly brackets), then the minimum length of the longest stem in the range '
                   '(in square brackets), a on each side of the filter. If a number of mismatches'
                    'is specified, every nucleotide that is not base paired acts like a mismatch. '
                   'Longest stem length is defined as the length of the longest continuous stretch of base paired '
                   'nucleotides (with no mismatches or bulges). Can also be a path to a file containing a list.'
                    'of descriptions to filter by.')
@click.option('-s', '--description_element_types', default='biotype:::biotype',
              help='The types of the description elements in the description filters, separated by :::. '
                   'Default is biotype:::biotype. Can also choose gene_id, transcript_id, gene_name or feature '
                   'on either side. Descriptions can be long form (e.g. gene_name:::biotype) or short form, '
                   'where each element is a single letter and no colons are required (e.g. nb). '
                   'Short forms are n for gene_name,b for biotype, f for feature, i for gene_id, '
                   'and t for transcript_id.')
@click.option('-l', '--lenient', is_flag=True,
              help='Flag to indicate that all hybrids that overlap the specified region of interest '
                   'should be returned. Default is false, indicating that only hybrids completely contained within '
                   'the region of interest are returned.')
@click.option('-d', '--directional', is_flag=True,
              help='Specifying this option tells the script to filter out hybrids involving the genes matching one or '
                   'more description filters in a different order.')
@click.option('-gt', '--remove_gt_pairing', is_flag=True,
              help='Flag to indicate that gt pairing should not be counted as valid base '
                   'pairing in viennad files. Default is False.')
@click.option('-v', '--invert', is_flag=True,
              help='Select the hybrids that match the filters rather than filtering them out.')
def filter(input_filepath, type, deltag, invert, description_filter,
           description_element_types, lenient, directional, remove_gt_pairing):
    """Filter a hyb file."""
    from hybtools.hybfilter import HybridType

    if type.lower().startswith('inter'):
        filter_type = HybridType.INTERMOLECULAR
    elif type.lower().startswith('intra'):
        filter_type = HybridType.INTRAMOLECULAR
    else:
        filter_type = HybridType.ALL

    commands.filter_hyb(
        hyb_filepath=input_filepath,
        hybrid_type=filter_type,
        dg=deltag,
        description_filter=description_filter,
        description_element_types=description_element_types,
        lenient=lenient,
        directional=directional,
        invert=invert
    ).pipe(write_tsv)
