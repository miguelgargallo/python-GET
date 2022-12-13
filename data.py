import requests

# Set the URL of the website you want to log
url = 'https://jutge.org/competitions/EDA:EDA_Q1_2022_23/rounds'

# Send a GET request to the website and store the response
response = requests.get(url)

# Print the status code of the response (should be 200 if the request was successful)
print(f'Status code: {response.status_code}')

# Print the contents of the website
print(response.text)
