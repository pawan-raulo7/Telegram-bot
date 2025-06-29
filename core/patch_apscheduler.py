# core/patch_apscheduler.py

import pytz
from apscheduler import util as aps_util

def patched_astimezone(obj):
    if isinstance(obj, str):
        try:
            return pytz.timezone(obj)
        except pytz.UnknownTimeZoneError:
            raise ValueError(f"Unknown timezone: {obj}")
    elif hasattr(obj, 'tzinfo') and obj.tzinfo is not None:
        return obj
    else:
        return pytz.UTC  # default fallback if no timezone is provided

# Override the internal function
aps_util.astimezone = patched_astimezone
