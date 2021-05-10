# -*- Mode: Python -*-

import logging
from datefile import parse_dates_in_filepath
from dateutils import next_month
from fileutils import sync_mtime_with_name_date, process_filenames

def parse_dates_in_filenames(args):
    dated = process_filenames(args.dir, parse_dates_in_filepath)
    prev_filename_date = dated[0].name_date
    for date_file in dated:
        expected = next_month(prev_filename_date)
        while expected < date_file.name_date:
            logging.warn('missing {0}/{1:02d}'.format(expected.year, expected.month))
            expected = next_month(expected)
        if args.touch:
            sync_mtime_with_name_date(date_file)
        date_file.verbose_log_result()
        prev_filename_date = date_file.name_date

    expected = next_month()
    while True:
        prev_filename_date = next_month(prev_filename_date)
        if prev_filename_date < expected:
            logging.warn('missing {0}/{1:02d}'.format(prev_filename_date.year, prev_filename_date.month))
        else:
            break
