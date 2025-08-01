import time

from faker import Faker
import httpx  

fake = Faker()
base_url = "http://localhost:8003/api/v1"

create_user_payload = {
    "email": fake.ascii_company_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}


# Выполняем запрос на создание пользователя
create_user_response = httpx.post(f"{base_url}/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Шаг 2. Открытие дебетового счёта
open_credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}
open_credit_card_account_response = httpx.post(
    f"{base_url}/accounts/open-credit-card-account",
    json=open_credit_card_account_payload
)

open_credit_card_account_response_data = open_credit_card_account_response.json()

make_purchase_payload = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": open_credit_card_account_response_data["account"]["cards"][0]["id"],
  "accountId": open_credit_card_account_response_data["account"]["id"],
  "category": "taxi"
}

make_purchase_response = httpx.post(
    f"{base_url}/operations/make-purchase-operation",
    json=make_purchase_payload
)
make_purchase_response_json = make_purchase_response.json()

print(make_purchase_response_json)

time.sleep(5) 

get_reciept_response = httpx.get(f"{base_url}/operations/operation-receipt/{make_purchase_response_json["operation"]["id"]}")

get_reciept_response_json = get_reciept_response.json()

print(get_reciept_response_json)

