from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def prettify_website():
    url = "http://example.com"  # Replace with your website URL
    admin_password = "ADMIN"  # Change this to the actual admin password

    user_input = input("Enter password: ")

    if user_input == admin_password:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            prettified_html = soup.prettify()
            return prettified_html
        else:
            return f"Failed to fetch website. Status code: {response.status_code}"
    else:
        return "Access denied."

if __name__ == "__main__":
    app.run(debug=True)
