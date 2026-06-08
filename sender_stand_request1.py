import configurations
import requests
 
 
def create_order(body):
    return requests.post(configurations.URL_SERVICE + configurations.CREATE_ORDERS,
                         json=body, timeout=10)
 
 
def get_order(track_number):
    get_order_url = f"{configurations.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    return requests.get(get_order_url, timeout=10)

