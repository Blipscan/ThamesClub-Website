import urllib.request

url = "https://calendar.google.com/calendar/ical/thamesclub.nl%40gmail.com/public/basic.ics"
ics = urllib.request.urlopen(url).read().decode("utf-8", errors="replace")

for block in ics.split("BEGIN:VEVENT")[1:8]:
    print("----- EVENT -----")
    for line in block.splitlines():
        if line.startswith(("SUMMARY", "DTSTART", "DTEND")):
            print(line)
