import requests
from bs4 import BeautifulSoup

# URLs
login_url = "http://xyz/"  # Replace with the actual login page URL
protected_url = "http://2xyz"  # Replace with the protected page URL

# Credentials
payload = {
    "txtusername": "xxxxxxxxxx",
    "txtpass": "xxxxxxxx",
    "btnlogin": "Login"
}

# Start a session
session = requests.Session()

# Step 1: Get the login page to retrieve hidden fields
response = session.get(login_url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Extract hidden fields
hidden_fields = ["__VIEWSTATE", "__VIEWSTATEGENERATOR", "__EVENTVALIDATION"]
for field in hidden_fields:
    payload[field] = soup.find("input", {"name": field})["value"]

# required fields
payload["__LASTFOCUS"] = ""
payload["__EVENTTARGET"] = ""
payload["__EVENTARGUMENT"] = ""

# Step 3: Submit the login form
login_response = session.post(login_url, data=payload)

# Check if login was successful
if "dashboard" in login_response.text.lower() or "logout" in login_response.text.lower():
    print("Login successful!")

    # Access the protected page
    response = session.get(protected_url)

    # Save the protected page HTML
    with open("protected_page.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    print("Protected page saved!")
else:
    print("Login failed!")
    print("Response:", login_response.text)
