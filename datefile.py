# -*- Mode: Python -*-

import os
import re
import logging
from strutils import atoi
from dateutils import file_date_to_datetime

class DateFile:
    def __init__(self, filepath):
        self.filepath = filepath
        parent, filename = os.path.split(filepath)
        self.filename = filename
        basename, ext = os.path.splitext(filename)
        parts = re.split('[ _-]', basename)

        date_parts = []
        self.string_parts = []

        for part in parts:
            nval = atoi(part)
            if nval:
                date_parts.append(nval)
            else:
                self.string_parts.append(part)

        if len(date_parts) == 2:
            year, month = date_parts
            self.name_date = file_date_to_datetime(year, month, 28)
        elif len(date_parts) == 3:
            year, month, day = date_parts
            self.name_date = file_date_to_datetime(year, month, day)
        else:
            self.name_date = None

    def __str__(self):
        return '<{}: {} / {}>'.format('DateFile', self.filename, self.name_date)

    def verbose_log_result(self):
        logging.debug('{}: month: {}, day: {}, year: {}'
                      .format(self.filename, self.name_date.month,
                              self.name_date.day, self.name_date.year))

def parse_dates_in_filepath(filepath):
    date_file = DateFile(filepath)
    if date_file.name_date:
        return date_file
    else:
        logging.debug('date not found in {}'.format(filepath))
        return None
