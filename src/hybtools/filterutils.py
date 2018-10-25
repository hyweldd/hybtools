"""Module containing utility functions related to filtering hyb and viennad files."""

# ______________________________________________________________________________
#
#     filterutils.py
#     Copyright (C) 2016  Hywel Dunn-Davies
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ______________________________________________________________________________

import collections
import itertools
import re

import pandas as pd


class DescriptionFilter(object):
    """Encapsulates logic for filtering based on description."""

    FilterBit = collections.namedtuple(
        'FilterBit',
        'feature   gene_id   transcript_id   gene_name   biotype   start   end   '
        'allowed_mismatches   min_longest_stem_length'
    )

    BitDetails = collections.namedtuple(
        'BitDetails',
        'description   start   end   dotplot'
    )

    filter_bit_regex = re.compile(
        r'^(?P<feature>[^\(\{\[]*)(\((?P<start>\d*)-((?P<end>\d*)\)))?(\(((?P<coord>\d*)\)))?'
        r'(\{(?P<allowed_mismatches>\d+)\})?(\[(?P<min_longest_stem_length>\d+)\])?$'
    )

    def __init__(self, description_filter, description_element_type, lenient):
        """Set up the Description Filter object."""
        # self.description_filter = description_filter
        # self.description_element_type = description_element_type
        # sys.exit(0)

        if description_filter:
            # print description_filter

            self.description_filter_bits = description_filter.strip().split(':::')
            # print self.description_filter_bits
            # sys.exit(0)
            assert len(self.description_filter_bits) == 2, 'unrecognised description filter: ' + str(description_filter)

            # print description_element_type
            self.description_element_type_bits = \
                DescriptionFilter.parse_description_element_type(description_element_type)

            self.filter_bits = list(map(self.parse_filter_bit, [1, 2]))
#            print(self.filter_bits)
#            sys.exit(0)

        self.lenient = lenient
        # self.bit1_description_filter = description_filter_parts[0]
        # self.bit2_description_filter = description_filter_parts[1]

    @staticmethod
    def parse_description_element_type(description_element_type):

        element_key = dict(
            b='biotype',
            f='feature',
            i='gene_id',
            n='gene_name',
            t='transcript_id'
        )

        # description_element_type_bits = None
        if len(description_element_type) == 2:
            description_element_type_bits = (
                element_key[description_element_type[0]],
                element_key[description_element_type[1]]
            )
            # sys.exit(0)
        else:
            description_element_type_bits = description_element_type.strip().split(':::')
            for index, description_element_type in enumerate(description_element_type_bits):
                # sys.exit(0)
                if description_element_type not in element_key.values():
                    description_element_type_bits[index] = element_key[description_element_type]
                # print index, description_element_type, element_key[description_element_type]

        assert len(description_element_type_bits) == 2, \
            'unrecognised description element type: ' + str(description_element_type)

        for description_element_type in description_element_type_bits:
            assert description_element_type in element_key.values()
        return description_element_type_bits

    def parse_filter_bit(self, bit):

        # print bit
        # sys.exit(0)

        feature, gene_id, transcript_id, gene_name, biotype = itertools.repeat(None, 5)

        filter_bit_string = self.description_filter_bits[bit-1]
        description_element_type = self.description_element_type_bits[bit-1]

        # print 'test'
        filter_bit_match = DescriptionFilter.filter_bit_regex.match(filter_bit_string)

        try:
            start = filter_bit_match.group('start')
            end = filter_bit_match.group('end')
            # print start, end
            #
            coord = filter_bit_match.group('coord')
            # print start, end, coord
            # sys.exit(0)
            allowed_mismatches = filter_bit_match.group('allowed_mismatches')
            min_longest_stem_length = filter_bit_match.group('min_longest_stem_length')
            # print 'min_longest_stem_length: ' + str(min_longest_stem_length)
            # sys.exit(0)
        except AttributeError:
            raise ValueError('Error, filter bit not recognised: ' + filter_bit_string)

        if start is None and end is None and coord is not None:
            start = coord
            end = coord

        if description_element_type == 'feature':
            feature = filter_bit_match.group('feature')
            # gene_id, transcript_id, gene_name, biotype = feature.split('_')
        elif description_element_type == 'gene_id':
            gene_id = filter_bit_match.group('feature')
        elif description_element_type == 'transcript_id':
            transcript_id = filter_bit_match.group('feature')
        elif description_element_type == 'gene_name':
            gene_name = filter_bit_match.group('feature')
        elif description_element_type == 'biotype':
            biotype = filter_bit_match.group('feature')

        feature = filter_bit_match.group('feature')
        # print feature
        # print start
        #
        # print end
        # print feature, str(start), str(end)
        filter_bit = DescriptionFilter.FilterBit(
            feature, gene_id, transcript_id, gene_name, biotype, start, end, allowed_mismatches, min_longest_stem_length
        )

        return filter_bit

    @staticmethod
    def filter_bit_is_empty(filter_bit):
        return filter_bit.feature is None and \
               filter_bit.gene_id is None and \
               filter_bit.transcript_id is None and \
               filter_bit.gene_name is None and \
               filter_bit.biotype == ''

    def matches_bit_filter(self, bit_details, bit):

        # matches_element = False
        description_element_type = self.description_element_type_bits[bit-1]
        filter_bit = self.filter_bits[bit-1]
        if DescriptionFilter.filter_bit_is_empty(filter_bit):
            # if no filter bit is specified it always matches
            matches_element = True
        else:
            gene_id, transcript_id, gene_name, biotype = bit_details.description.split('_')
            if description_element_type == 'feature':
                matches_element = (bit_details.description == filter_bit.feature)
            elif description_element_type == 'gene_id':
                matches_element = (gene_id == filter_bit.gene_id)
            elif description_element_type == 'transcript_id':
                matches_element = (transcript_id == filter_bit.transcript_id)
            elif description_element_type == 'gene_name':
                matches_element = (gene_name == filter_bit.gene_name)
            elif description_element_type == 'biotype':
                matches_element = (biotype == filter_bit.biotype)
            else:
                raise ValueError('unrecognised description element type: ' + str(description_element_type))

        coordinates_matching = matches_element and self.coordinates_match(filter_bit, bit_details)

        # print 'matches_element: {matches_element}'.format(**locals())
        # print 'coordinates_matching: {coordinates_matching}'.format(**locals())
        #
        # print bit_details
        # print filter_bit
        #
        # sys.exit(0)

        # if filter_bit.allowed_mismatches is None and filter_bit.min_longest_stem_length is None:
        #     return coordinates_matching

        if filter_bit.allowed_mismatches is None:
            basepairing_matches = True
        else:

            assert bit_details.dotplot is not None, \
                'Dotplot line missing in bit: ' + str(bit_details) + \
                '. Filtering based on base pairing can only be carried out on valid viennad entries.'

            # check base pairing
            dotplot_range = range(
                min(int(filter_bit.start), int(bit_details.start)),
                max(int(filter_bit.end), int(bit_details.end)) + 1
            )
            dotplot_series = pd.Series(
                list(itertools.repeat('.', len(dotplot_range))),
                dotplot_range
            )

            dotplot_series.loc[int(bit_details.start):int(bit_details.end)] = list(bit_details.dotplot)
            filter_range_dotplot = dotplot_series.loc[int(filter_bit.start):int(filter_bit.end)]
            number_of_mismatches = len(filter_range_dotplot[filter_range_dotplot == '.'])

            basepairing_matches = (number_of_mismatches <= int(filter_bit.allowed_mismatches))

        # print 'basepairing_matches: {basepairing_matches}'.format(**locals())

        if filter_bit.min_longest_stem_length is None:
            min_longest_stem_matches = True
        else:
            # check minimum longest stem length

            assert bit_details.dotplot is not None, \
                'Dotplot line missing in bit: ' + str(bit_details) + \
                '. Filtering based on longest stem length can only be carried out on valid viennad entries.'

            # min_longest_stem_matches = True
            # print bit_details
            # print filter_bit

            # sliced_dotplot =  '0123456789' # bit_details.dotplot
            sliced_dotplot = bit_details.dotplot
            # print sliced_dotplot

            if filter_bit.start is not None:
                local_start = int(filter_bit.start) - int(bit_details.start)
                # print int(local_start)
                sliced_dotplot = sliced_dotplot[local_start:]

            # print sliced_dotplot

            if filter_bit.end is not None:
                local_end = int(filter_bit.end) - int(bit_details.start)
                # print int(local_end)
                sliced_dotplot = sliced_dotplot[:local_end-1]

            # print sliced_dotplot
            # sys.exit(0)

            current_stem_length = 0
            longest_stem_length = 0
            for character in sliced_dotplot:
                if character in ['(', ')']:
                    current_stem_length += 1
                else:
                    longest_stem_length = max(current_stem_length, longest_stem_length)
                    current_stem_length = 0
            longest_stem_length = max(current_stem_length, longest_stem_length)

            # print longest_stem_length
            # sys.exit(0)

            min_longest_stem_matches = (
                longest_stem_length >= int(filter_bit.min_longest_stem_length)
            )

        return coordinates_matching and basepairing_matches and min_longest_stem_matches

    def coordinates_match(self, filter_bit, bit_details):
        # return True
        if self.lenient:
            # lenient matching - all hybrids that overlap the region of interest are returned
            if filter_bit.start and filter_bit.end:
                return (
                    (int(bit_details.end) >= int(filter_bit.start)) and
                    (int(bit_details.start) <= int(filter_bit.end))
                )
            elif filter_bit.start and not filter_bit.end:
                return int(bit_details.end) >= int(filter_bit.start)
            elif not filter_bit.start and filter_bit.end:
                return int(bit_details.start) <= int(filter_bit.end)
            else:
                # there are no co-ordinates specified
                return True
        else:
            # strict matching - only hybrids completely contained within the region of interest are returned
            if filter_bit.start and filter_bit.end:
                return (
                    (int(bit_details.start) >= int(filter_bit.start)) and
                    (int(bit_details.end) <= int(filter_bit.end))
                )
            elif filter_bit.start and not filter_bit.end:
                return int(bit_details.start) >= int(filter_bit.start)
            elif not filter_bit.start and filter_bit.end:
                return int(bit_details.end) <= int(filter_bit.end)
            else:
                # there are no co-ordinates specified
                return True

    def should_exclude_hyb_record(self, hyb_record, directional=False):

        return not self.bit_details_match_filter(
            bit_1_details=DescriptionFilter.BitDetails(
                hyb_record.bit1_description,
                hyb_record.bit1_transcript_coordinates_start,
                hyb_record.bit1_transcript_coordinates_stop,
                None
            ),
            bit_2_details=DescriptionFilter.BitDetails(
                hyb_record.bit2_description,
                hyb_record.bit2_transcript_coordinates_start,
                hyb_record.bit2_transcript_coordinates_stop,
                None
            ),
            directional=directional
        )

    def should_exclude_viennad_record(self, viennad_record, directional=False):

            bit_1_details = DescriptionFilter.BitDetails(
                viennad_record.fragment_1_mapped_feature,
                viennad_record.fragment_1_transcript_start,
                viennad_record.fragment_1_transcript_end,
                viennad_record.fragment_1_dotplot
            )

            bit_2_details = DescriptionFilter.BitDetails(
                viennad_record.fragment_2_mapped_feature,
                viennad_record.fragment_2_transcript_start,
                viennad_record.fragment_2_transcript_end,
                viennad_record.fragment_2_dotplot
            )

            # print 'bit_1_details: {bit_1_details}'.format(**locals())
            # print 'bit_2_details: {bit_2_details}'.format(**locals())

            return not self.bit_details_match_filter(
                bit_1_details=bit_1_details,
                bit_2_details=bit_2_details,
                directional=directional
            )

    def bit_details_match_filter(self, bit_1_details, bit_2_details, directional=False):
        if self.matches_bit_filter(bit_1_details, bit=1) and \
                self.matches_bit_filter(bit_2_details, bit=2):
            return True
        elif not directional and self.matches_bit_filter(bit_1_details, bit=2) and \
                self.matches_bit_filter(bit_2_details, bit=1):
            return True
        else:
            return False
