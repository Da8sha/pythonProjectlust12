import sender_stand_request
def test_proverka_200():
    true_proverka =sender_stand_request.response_2
    assert true_proverka.status_code==200

