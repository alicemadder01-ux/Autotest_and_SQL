import configurations
import requests
import data

def create_order(body):
    return requests.post(configurations.URL_SERVICE + configurations.CREATE_ORDERS,
                         json=body,  timeout=10)


def get_order(track_number):
    get_order_url = f"{configurations.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url,  timeout=10)
    return response


def test_order_creation_and_retrieval():
    response = create_order(data.order_body)

    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)
    order_response = get_order(track_number)

    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)

# def test_get_order_by_track():
#     # Создаём заказ
#     create_response = requests.post(f"{configurations.URL_SERVICE}/api/v1/orders", json=data.order_body)
#     print  (create_response)
#     # Сохраняем номер трека
#     track = create_response.json()["track"]
#     print(track)
#     # Получаем заказ по треку
#     get_response = requests.get(f"{configurations.URL_SERVICE}/api/v1/orders/track", params={"t": track})
#     print (get_response)
#     # Проверяем, что код ответа 200
#     assert get_response.status_code == 200