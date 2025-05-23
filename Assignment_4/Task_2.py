# Write data to the file
user_input = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")
print("Your data has been successfully written to 'output.txt'.")

# Append additional data
append_input = input("Enter additional text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(append_input + "\n")
print("Your additional data has been successfully added to 'output.txt'.")

# Read and display the final content of the file
print("\nFinal content of your file:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
