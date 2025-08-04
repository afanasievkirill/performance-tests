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


create_user_response = httpx.post(f"{base_url}/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print("Create user response:", create_user_response_data)
print("Status Code:", create_user_response.status_code)

open_deposite_payload = {
  "userId": create_user_response_data['user']['id']
}

open_deposite_response = httpx.post(f"{base_url}/accounts/open-deposit-account", json=open_deposite_payload)
open_deposite_response_data = open_deposite_response.json()

print("Create deposite response:", open_deposite_response_data)
print("Status Code:", open_deposite_response.status_code)