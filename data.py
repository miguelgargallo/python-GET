import requests

# Set the URL of the website you want to log
url = 'https://jutge.org/competitions/EDA:EDA_Q1_2022_23/rounds'

# Send a GET request to the website and store the response
response = requests.get(url)

# Open a file for writing
with open('website_contents.pylar', 'w') as f:
    # Write the contents of the website to the file
    f.write(response.text)
