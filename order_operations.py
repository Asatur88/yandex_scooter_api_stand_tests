import requests
from configuration import API_BASE_URL
from data import order_data

def create_order():
    # Создаем URL для создания заказа
    create_order_url = f"{API_BASE_URL}/api/v1/orders"

    # Отправляем POST-запрос с данными о заказе и получаем ответ от сервера
    response_create_order = requests.post(create_order_url, json=order_data)

    # Возвращаем ответ от сервера
    return response_create_order

def get_order_by_track(track):
    # Создаем URL для получения заказа по трек-номеру
    get_order_url = f"{API_BASE_URL}/v1/orders/track?t={track}"

    # Отправляем GET-запрос для получения заказа по трек-номеру и получаем ответ от сервера
    response_get_order = requests.get(get_order_url)

    # Возвращаем ответ от сервера
    return response_get_order

