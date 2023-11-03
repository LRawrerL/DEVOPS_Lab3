import price_info


def test_total_cost_shopping():
    result = 0
    total_cost = 46.75

    result = price_info.total_cost_shopping()
    assert result == total_cost


def test_cost_of_fruits():
    result = 0
    type_of_fruit_in_list = 'orange'
    quantity = 5

    result = price_info.cost_of_fruits(type_of_fruit_in_list, quantity)
    assert result == 7.0
    assert (price_info.cost_of_fruits('apple', 3) == 3.6)



