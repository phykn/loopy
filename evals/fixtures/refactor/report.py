"""Build category totals and render them as text or JSON."""

import json
from decimal import Decimal


class ReportBuilder:
    def __init__(self, records, sort=True):
        self.records = records
        self.sort = sort

    def totals(self):
        if self.records is None:
            return {}
        totals = {}
        # Loop over records and add each amount to its category
        for record in self.records:
            category = record["category"].strip().lower()
            totals[category] = totals.get(category, Decimal("0")) + record["amount"]
        if self.sort:
            totals = dict(sorted(totals.items()))
        return totals

    def text(self):
        totals = self.totals()
        lines = [f"{category} {amount:.2f}" for category, amount in totals.items()]
        # Add the total line
        lines.append(f"total {sum(totals.values(), Decimal('0')):.2f}")
        return "\n".join(lines)

    def write_json(self, path):
        totals = self.totals()
        data = {
            "categories": {category: f"{amount:.2f}" for category, amount in totals.items()},
            "total": f"{sum(totals.values(), Decimal('0')):.2f}",
        }
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
