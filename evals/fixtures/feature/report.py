import json
from decimal import Decimal


def sum_by_category(records):
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, Decimal("0")) + record["amount"]
    return dict(sorted(totals.items()))


def render_text(totals):
    lines = [f"{category} {amount:.2f}" for category, amount in totals.items()]
    lines.append(f"total {grand_total(totals):.2f}")
    return "\n".join(lines)


def write_json(totals, path):
    data = {
        "categories": {category: f"{amount:.2f}" for category, amount in totals.items()},
        "total": f"{grand_total(totals):.2f}",
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def grand_total(totals):
    return sum(totals.values(), Decimal("0"))
