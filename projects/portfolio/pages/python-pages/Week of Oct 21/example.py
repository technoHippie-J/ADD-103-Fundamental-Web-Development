# Import the requests package
import requests

# Make a GET request to a website
response = requests.get('https://api.github.com')

# Print the status code (should be 200 if the request is successful)
print(response.status_code)
