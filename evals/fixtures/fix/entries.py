import re

ENTRY = re.compile(r"([0-9]{2}):([0-9]{2})-([0-9]{2}):([0-9]{2}) (.+)")


def read_entries(path):
    entries = []
    with open(path, encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            match = ENTRY.fullmatch(line)
            if not match:
                raise ValueError(f"line {number}: expected HH:MM-HH:MM task")
            start = to_minutes(match[1], match[2])
            end = to_minutes(match[3], match[4])
            if start is None or end is None:
                raise ValueError(f"line {number}: time must be between 00:00 and 23:59")
            entries.append((match[5], end - start))
    return entries


def to_minutes(hours, minutes):
    hours = int(hours)
    minutes = int(minutes)
    if hours > 23 or minutes > 59:
        return None
    return hours * 60 + minutes
