# Open the file in read mode
file_name = "name.txt"
try:
    with open(file_name, 'r') as file:
        # Read and print each line in the file
        for line in file:
            print(line, end='')  # Use end='' to prevent extra newlines
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
