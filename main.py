# Виктория Доржиева, 9-я когорта - Финальный проект. Инженер по тестированию плюс
import orders


def something_wrong_here(a, b):
    if a == b:
        print('Тест пройден')
    else:
        print('Тест провален')


something_wrong_here(orders.post_data_order_by_track(orders.post_track_order()).status_code, 200)
