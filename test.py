import orders


def test_get_order_by_track():
    track = orders.post_track_order()
    data_orders = orders.post_data_order_by_track(track)

    assert data_orders.status_code == 200
