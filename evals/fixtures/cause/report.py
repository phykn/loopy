def stock_by_item(moves):
    stock = {}
    for item, quantity in moves:
        stock[item] = stock.get(item, 0) + quantity
    return stock


def render(stock):
    lines = [f"{item} {count}" for item, count in stock.items()]
    lines.append(f"total {sum(stock.values())}")
    return "\n".join(lines)
