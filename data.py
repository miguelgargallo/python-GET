import os
import requests

# Set the base URL for the website
base_url = "https://jutge.org/competitions/EDA:EDA_Q1_2022_23/rounds/"

# Create the pylar.data folder if it doesn't already exist
if not os.path.exists("pylar.data"):
    os.mkdir("pylar.data")

# Loop through values from 1 to 143
for value in range(1, 144):
    # Compose the URL for the current value
    url = base_url + str(value)

    # Check if the file for the current URL already exists in the pylar.data folder
    # If it does, skip downloading it again
    if os.path.exists(os.path.join("pylar.data", str(value))):
        print(f"Skipping {url} - file already exists")
        continue

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the server returned a 200 OK status code
    # If it didn't, skip downloading the file
    if response.status_code != 200:
        print(
            f"Skipping {url} - server returned status code {response.status_code}")
        continue

    # Save the file in the pylar.data folder
    with open(os.path.join("pylar.data", str(value)), "w") as f:
        f.write(response.text)
        print(f"Saved {url}")
