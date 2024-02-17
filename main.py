import requests
from bs4 import BeautifulSoup

def prettify_website(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the website
        soup = BeautifulSoup(response.content, 'html.parser')

        # Prettify the HTML content
        prettified_html = soup.prettify()

        return prettified_html
    else:
        print(f"Failed to fetch website. Status code: {response.status_code}")
        return None

def main():
    url = "http://example.com"
    admin_password = "ADMIN"  # Change this to the actual admin password

    user_input = input("Enter password: ")

    if user_input == admin_password:
        prettified_html = prettify_website(url)
        if prettified_html:
            # Save or display the prettified HTML content
            print(prettified_html)
            # You can also save the prettified_html to a file if needed
            # with open("prettified.html", "w") as file:
            #     file.write(prettified_html)
    else:
        print("Access denied.")

if __name__ == "__main__":
    main()
#MAKE SURE TODO pip install requests beautifulsoup4
