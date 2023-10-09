import orders


def test_get_order_by_track():
    track = orders.get_track_order()
    data_orders = orders.get_data_order_by_track(track)

    assert data_orders.status_code == 200
