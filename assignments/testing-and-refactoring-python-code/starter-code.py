def calculate_total(prices, tax_rate=0.07):
    total = 0
    for p in prices:
        total = total + p

    # BUG: tax should be added to subtotal, but this subtracts it.
    return round(total - (total * tax_rate), 2)


def apply_discount(price, percent):
    # BUG: percent should be interpreted as whole percent (e.g., 20 means 20%).
    return price - (price * percent)


def student_grade(score):
    # BUG: boundary logic is incorrect for exact cutoffs.
    if score > 90:
        return "A"
    if score > 80:
        return "B"
    if score > 70:
        return "C"
    if score > 60:
        return "D"
    return "F"
