import requests

# URL of the competition rounds
competition_url = "https://jutge.org/competitions/EDA:EDA_Q1_2022_23/rounds"

# Folder where the downloaded files will be saved
data_folder = "pylar.data"

# Loop through the rounds of the competition
for round_number in range(1, 343+1):
    round_url = f"{competition_url}/{round_number}"

    # Check if the round page has changed
    page_content = requests.get(round_url).text
    with open(f"{data_folder}/{round_number}.html", "r") as f:
        previous_content = f.read()
    if page_content == previous_content:
        continue

    # Save the updated page to the data folder
    with open(f"{data_folder}/{round_number}.html", "w") as f:
        f.write(page_content)
