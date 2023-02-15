import configuration
import requests
import data

def post_new_order(data): #создание заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_ORDER,  # подставялем полный url
                         json=data.user_order) # тут тело

response = post_new_order(data)
print(response.json()) # вывод ответа

def order_track(): #функция на получение заказа по треку
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_TRACK,
                        params={"t":response.json()['track']})

response_2= order_track()
print(response_2.json()) # вывод ответа
