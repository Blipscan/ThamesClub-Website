import json
import re
import urllib.request
from datetime import datetime, timedelta, time
from zoneinfo import ZoneInfo

ICAL_URL = "https://calendar.google.com/calendar/ical/thamesclub.nl%40gmail.com/public/basic.ics"
LOCAL_TZ = ZoneInfo("America/New_York")

def unfold_ics(text):
    # ICS folded lines start with a space or tab; join them back
    return re.sub(r"\r?\n[ \t]", "", text)

def clean(s):
    return (
        s.replace("\\n", " ")
         .replace("\\,", ",")
         .replace("\\;", ";")
         .replace("\\:", ":")
         .strip()
    )

def get_field(block, name):
    # captures both DTSTART:... and DTSTART;TZID=America/New_York:...
    m = re.search(rf"^{name}([^:]*)[:](.*)$", block, re.MULTILINE)
    if not m:
        return None, None
    return m.group(1), m.group(2).strip()

def parse_google_dt(params, value):
    params = params or ""

    # All-day event
    if "T" not in value:
        d = datetime.strptime(value[:8], "%Y%m%d").date()
        return datetime.combine(d, time.min).replace(tzinfo=LOCAL_TZ), True

    # UTC event
    if value.endswith("Z"):
        d = datetime.strptime(value, "%Y%m%dT%H%M%SZ")
        return d.replace(tzinfo=ZoneInfo("UTC")).astimezone(LOCAL_TZ), False

    # TZID event
    tz_match = re.search(r"TZID=([^;:]+)", params)
    if tz_match:
        tz = ZoneInfo(tz_match.group(1))
    else:
        tz = LOCAL_TZ

    d = datetime.strptime(value[:15], "%Y%m%dT%H%M%S")
    return d.replace(tzinfo=tz).astimezone(LOCAL_TZ), False

ics = urllib.request.urlopen(ICAL_URL).read().decode("utf-8", errors="ignore")
ics = unfold_ics(ics)

today = datetime.now(LOCAL_TZ).date()
cutoff = today + timedelta(days=30)

events = []

for block in ics.split("BEGIN:VEVENT")[1:]:
    summary_params, summary = get_field(block, "SUMMARY")
    desc_params, desc = get_field(block, "DESCRIPTION")
    dt_params, dt_value = get_field(block, "DTSTART")

    if not summary or not dt_value:
        continue

    start, all_day = parse_google_dt(dt_params, dt_value)

    if start.date() < today or start.date() > cutoff:
        continue

    if all_day:
        date_text = start.strftime("%A · %B %#d")
    else:
        date_text = start.strftime("%A · %B %#d · %#I:%M %p")

    events.append({
        "title": clean(summary),
        "date": date_text,
        "description": clean(desc) if desc else "",
        "image": "images/events_01.jpg",
        "sort": start.isoformat()
    })

events.sort(key=lambda x: x["sort"])

for e in events:
    del e["sort"]

with open("events.json", "w", encoding="utf-8") as f:
    json.dump(events, f, indent=2, ensure_ascii=False)

print(f"Updated events.json with {len(events)} events.")
