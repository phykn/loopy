def total_by_task(entries):
    totals = {}
    for task, minutes in entries:
        totals[task] = totals.get(task, 0) + minutes
    return totals


def render(totals):
    lines = [f"{task} {format_minutes(minutes)}" for task, minutes in totals.items()]
    lines.append(f"total {format_minutes(sum(totals.values()))}")
    return "\n".join(lines)


def format_minutes(minutes):
    hours, minutes = divmod(minutes, 60)
    return f"{hours}:{minutes:02d}"
