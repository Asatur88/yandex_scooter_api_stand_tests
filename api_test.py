from order_operations import create_order, get_order_by_track

def test_create_and_get_order():
    # Создаем заказ и проверяем успешное создание
    response_create_order = create_order()
    assert response_create_order.status_code == 201  # Проверяем, что статус код равен 201 (Успешное создание заказа)
    order_track = response_create_order.json()["track"]  # Получаем трек-номер созданного заказа

    # Получаем заказ по трек-номеру и проверяем успешное получение
    response_get_order = get_order_by_track(order_track)
    assert response_get_order.status_code == 200  # Проверяем, что статус код равен 200 (Успешное получение заказа)

