from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client

users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
document_gateway_client = build_documents_gateway_http_client()

# Создаем пользователя
create_user_response = users_gateway_client.create_user()
print("Create user response:", create_user_response)

# Создаем крелитный счет
create_account_response = accounts_gateway_client.open_credit_card_account(
    user_id=create_user_response.user.id
)

print("Open credit card account response:", create_account_response)

# получкаем ссылку на информацию по тарифу
get_tariff_document_response = document_gateway_client.get_tariff_document(
    account_id=create_account_response.account.id
)

print("Get tariff document response:", get_tariff_document_response)

# получкаем ссылку на информацию по контракту
get_contract_document_response = document_gateway_client.get_contract_document(
    account_id=create_account_response.account.id
)

print("Get contract document response:", get_contract_document_response)