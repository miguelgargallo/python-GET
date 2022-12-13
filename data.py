import requests
import os

# URL of the competition rounds
competition_url = "https://jutge.org/competitions/EDA:EDA_Q1_2022_23/rounds"

# Folder where the downloaded files will be saved
data_folder = "pylar.data"

# Check if the data folder exists, and create it if it doesn't
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Loop through the rounds of the competition
for round_number in range(1, 242+1):
    round_url = f"{competition_url}/{round_number}"

    # Check if the round page has changed
    page_content = requests.get(round_url).text

    # If the file already exists, check if it has been updated
    if os.path.exists(f"{data_folder}/{round_number}.pylar"):
        with open(f"{data_folder}/{round_number}.pylar", "r") as f:
            previous_content = f.read()
        if page_content == previous_content:
            # If the page hasn't changed, skip this round
            continue

    # If the file doesn't exist or the page has changed, update the file in the data folder
    with open(f"{data_folder}/{round_number}.pylar", "w") as f:
        f.write(page_content)
