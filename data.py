import requests
import os
import csv

# URL of the competition rounds
competition_url = "https://jutge.org/competitions/EDA:EDA_Q1_2022_23/rounds"

# Folder where the downloaded files will be saved
data_folder = "pylar.data"

# Check if the data folder exists, and create it if it doesn't
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Loop through the rounds of the competition
for round_number in range(1, 343+1):
    round_url = f"{competition_url}/{round_number}"

    # Check if the round page has changed
    page_content = requests.get(round_url).text
    if not os.path.exists(f"{data_folder}/{round_number}.pylar"):
        # If the file doesn't exist, download it
        with open(f"{data_folder}/{round_number}.pylar", "w") as f:
            f.write(page_content)
    else:
        # If the file already exists, check if it has been updated
        with open(f"{data_folder}/{round_number}.pylar", "r") as f:
            previous_content = f.read()
        if page_content == previous_content:
            continue

        # If the page has changed, update the file in the data folder
        with open(f"{data_folder}/{round_number}.pylar", "w") as f:
            f.write(page_content)

    # Extract the table data from the page content
    table_data = []
    for line in page_content.split("\n"):
        if "<td>" in line:
            # Parse the line into a list of table cells
            cells = [cell.strip() for cell in line.
                    