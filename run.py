# Specify the path to your input text file
from day01 import p1
from day01 import p2

file_path = 'day01.txt'

try:
    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        # Read the entire content of the file
        file_content = file.read()

        # Print or process the content as needed
        print(p1(file_content))
        print(p2(file_content))

except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
