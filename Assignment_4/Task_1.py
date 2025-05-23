try:
    with open("sample.txt", "r") as file:
        print("File content:")
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
