# -*- Mode: Python -*-

import os
from dateutils import datetime_to_timestamp

def sync_mtime_with_name_date(date_file):
    filename = date_file.filename
    name_date = date_file.name_date

    timestamp = datetime_to_timestamp(name_date)
    stinfo = os.stat(filename)
    os.utime(filename, (stinfo.st_atime, timestamp))

def process_filenames(dirpath, processor):
    files = os.listdir(dirpath)
    processed_with_none = [processor(filepath) for filepath in files]
    processed = [date_file for date_file in processed_with_none if date_file]
    return sorted(processed, key=lambda df: df.name_date)
