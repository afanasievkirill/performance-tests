from faker import Faker
import httpx  # Импортируем HTTPX


fake = Faker()
base_url = "http://localhost:8003/api/v1"

# Шаг 1. Создание пользователя
create_user_payload = {
    "email": fake.ascii_company_email(),  # Уникальный email с timestamp
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post(f"{base_url}/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Шаг 2. Открытие дебетового счёта
open_debit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}
open_debit_card_account_response = httpx.post(
    f"{base_url}/accounts/open-debit-card-account",
    json=open_debit_card_account_payload
)
open_debit_card_account_response_data = open_debit_card_account_response.json()

# Шаг 3. Выпуск виртуальной карты
issue_virtual_card_payload = {
    "userId": create_user_response_data["user"]["id"],
    "accountId": open_debit_card_account_response_data["account"]["id"]
}
issue_virtual_card_response = httpx.post(
    f"{base_url}/cards/issue-virtual-card",
    json=issue_virtual_card_payload
)
issue_virtual_card_response_data = issue_virtual_card_response.json()

# Выводим результат
print("Issue virtual card response:", issue_virtual_card_response_data)
print("Issue virtual card status code:", issue_virtual_card_response.status_code)