import hashlib
import os

def calculate_hash(file_name):
    with open(file_name, "rb") as file:
        data = file.read()
        return hashlib.sha256(data).hexdigest()


print("=== FILE INTEGRITY CHECKER ===")
print("1. Save file hash")
print("2. Check file integrity")

choice = input("Enter choice (1 or 2): ")
filename = input("Enter file name: ")

if not os.path.exists(filename):
    print("Error: File does not exist.")
    exit()

if choice == "1":
    hash_value = calculate_hash(filename)
    with open("hash_record.txt", "w") as record:
        record.write(filename + "|" + hash_value)
    print("Hash saved successfully.")

elif choice == "2":
    if not os.path.exists("hash_record.txt"):
        print("No hash record found. Save hash first.")
    else:
        with open("hash_record.txt", "r") as record:
            saved_filename, saved_hash = record.read().split("|")

        current_hash = calculate_hash(filename)

        if current_hash == saved_hash:
            print("File integrity intact. No changes detected.")
        else:
            print("WARNING! File has been modified.")

else:
    print("Invalid choice.")


