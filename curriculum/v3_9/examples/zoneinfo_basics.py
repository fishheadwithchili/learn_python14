"""zoneinfo basics: IANA time zones from the standard library.

Run with Python >=3.9
"""

from datetime import datetime
from zoneinfo import ZoneInfo

now_utc = datetime.now(tz=ZoneInfo("UTC"))
tokyo = now_utc.astimezone(ZoneInfo("Asia/Tokyo"))
new_york = now_utc.astimezone(ZoneInfo("America/New_York"))

print("UTC:", now_utc)
print("Tokyo:", tokyo)
print("New York:", new_york)


