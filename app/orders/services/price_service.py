
def count_price_for_order(order_list):
    price = 0

    for item in order_list.all():
        price += item.price

    return price