import data
import sender_stand_request
def test_proverka_sozdanie_zakaza_200():
    create_order_response = sender_stand_request.post_new_order(data)
    assert create_order_response.status_code == 201 , "Ошибка создания заказа"

def test_nalichie_nomera_treka():
    assert (sender_stand_request.response.json())

def test_poluchienie_nomera_treka():
    print (sender_stand_request.response.json())

def test_proverka_200():
    true_proverka =sender_stand_request.response_2
    assert true_proverka.status_code==200

