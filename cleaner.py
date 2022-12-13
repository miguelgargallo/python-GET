import os

# Path to the folder containing the files
folder_path = "pylar.data"

# Get a list of all files in the folder
file_list = os.listdir(folder_path)

# Loop through each file in the folder
for file_name in file_list:
    # Full path to the file
    file_path = os.path.join(folder_path, file_name)

    # Open the file in read mode
    with open(file_path, "r") as file:
        # Read the contents of the file
        file_content = file.read()

        # Clean the content inside the <head> tag
        cleaned_content = file_content.replace("<head>", "").replace("</head>", "")

    # Open the file in write mode
    with open(file_path, "w") as file:
        # Write the cleaned content to the file
        file.write(cleaned_content)
