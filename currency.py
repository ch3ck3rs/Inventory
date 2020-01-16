def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)


def as_thousands(x):
    return "${:.1f}K".format(x / 1000)
