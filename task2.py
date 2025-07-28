def write_to_file(filename):
    user_input = input("Enter text to write to the file: ")
    try:
        with open(filename, 'w') as file:
            file.write(user_input + '\n')
        print(f"Initial data written to '{filename}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def append_to_file(filename):
    additional_input = input("Enter additional text to append: ")
    try:
        with open(filename, 'a') as file:
            file.write(additional_input + '\n')
        print(f"Additional data appended to '{filename}'.")
    except Exception as e:
        print(f"Error appending to file: {e}")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"\nFinal contents of '{filename}':")
            for line in file:
                print(line.strip())
    except Exception as e:
        print(f"Error reading file: {e}")

filename = 'output.txt'

write_to_file(filename)
append_to_file(filename)
read_file(filename)
