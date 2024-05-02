#!/usr/bin/env python

import sys
from datetime import datetime, timedelta, tzinfo
from calendar import timegm

# Constants for converting between datetime and Windows filetime
EPOCH_AS_FILETIME = 116444736000000000  # January 1, 1970 as MS file time
HUNDREDS_OF_NANOSECONDS = 10000000

# Define zero and hour timedelta for time adjustment
ZERO = timedelta(0)
HOUR = timedelta(hours=1)

class UTC(tzinfo):
    """UTC Timezone class"""
    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO

# Create a UTC timezone object
utc = UTC()

def dt_to_filetime(dt):
    """Converts a datetime to Microsoft filetime format. If the object is
    time zone-naive, it is forced to UTC before conversion.
    """
    if (dt.tzinfo is None) or (dt.tzinfo.utcoffset(dt) is None):
        dt = dt.replace(tzinfo=utc)
    return EPOCH_AS_FILETIME + (timegm(dt.timetuple()) * HUNDREDS_OF_NANOSECONDS)

def filetime_to_dt(ft):
    """Converts a Microsoft filetime number to a Python datetime. The new
    datetime object is time zone-naive but is equivalent to tzinfo=utc.
    """
    return datetime.utcfromtimestamp((ft - EPOCH_AS_FILETIME) / HUNDREDS_OF_NANOSECONDS)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If a filetime is provided as an argument, convert it to datetime
        filetime = int(sys.argv[1])
        datetime_from_filetime = filetime_to_dt(filetime)
        print(f"Filetime {filetime} converted to datetime: {datetime_from_filetime}")
    else:
        # Default behavior using the current datetime
        current_datetime = datetime.now()
        file_time = dt_to_filetime(current_datetime)
        print(f"Current datetime: {current_datetime} converted to filetime: {file_time}")

        # Convert back to datetime to verify
        converted_datetime = filetime_to_dt(file_time)
        print(f"Filetime: {file_time} converted back to datetime: {converted_datetime}")
