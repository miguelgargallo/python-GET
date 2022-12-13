import os

# Set the directory path
directory = "pylar.data"

# Loop through all files in the directory
for filename in os.listdir(directory):
  # Open the file in read mode
  with open(os.path.join(directory, filename), "r") as file:
    # Read the first 7902 lines
    for _ in range(7902):
      file.readline()

    # Read the next 189 lines and discard them
    for _ in range(189):
      file.readline()

    # Read the rest of the file
    data = file.read()

  # Open the file in write mode
  with open(os.path.join(directory, filename), "w") as file:
    # Overwrite the file with the remaining data
    file.write(data)
