import re

MOVE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2} ([a-z]+) ([0-9]+) (.+)")
KINDS = ("in", "out", "return")


def read_moves(path):
    moves = []
    with open(path, encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            match = MOVE.fullmatch(line)
            if not match:
                raise ValueError(f"line {number}: expected YYYY-MM-DD kind quantity item")
            kind, quantity, item = match[1], int(match[2]), match[3]
            if kind not in KINDS:
                raise ValueError(f"line {number}: unknown kind {kind!r}")
            if quantity == 0:
                raise ValueError(f"line {number}: quantity must be at least 1")
            if kind in ("out", "return"):
                quantity = -quantity
            moves.append((item, quantity))
    return moves
