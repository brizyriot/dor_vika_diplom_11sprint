import requests
import configuration
import data


def get_track_order():
    order = requests.post(configuration.URL + configuration.CREATE,
                          json=data.orders_body
                          )
    new_track = order.json()["track"]
    return new_track


def get_data_order_by_track(track):
    return requests.get(configuration.URL + configuration.TRACK,
                        params={"t": track}
                        )