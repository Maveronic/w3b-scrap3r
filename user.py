import requests
import json
import os

# Set up credentials for accessing your account
# Best practice we will require using environment variables
# or making use of a secrets file. In this case, I will be 
# using my environment variables
BASE_URL = "https://api.multilogin.com"
LOGIN_ENDPOINT = "/user/signin"
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Define the login function
def login_and_get_token():
    login_url = BASE_URL + LOGIN_ENDPOINT
    payload = {"email": EMAIL, "password": PASSWORD}
    response = requests.post(login_url, json=payload)
    
    if response.status_code == 200:
        print("Login successful!")
        response_data = response.json()
        token = response_data["data"]["token"]
        return token
    else:
        print("Login failed:", response.json())
        return None

# Define the function to create a quick profile
def get_quick_profile():
    pass


# The program entry point
def main():
    # Step 1: Log in to get authentication token
    token = login_and_get_token()
    if token:
        print(f"Retrieved Token: {token}")
if __name__ == "__main__":
    main()
