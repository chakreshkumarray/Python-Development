
import os

file_name = "notes.txt"

# ✅ Check if file exists
if not os.path.exists(file_name):
    # Create file and write initial content
    with open(file_name, "w") as file:
      file.write("This is a new file.\n")
      file.write("File created successfully.\n")
    print("🆕 File created and data written.")
else:
    print("📄 File already exists.")

# Read the file
with open(file_name, "r") as file:
  print("\n--- Current File Content ---")
  print(file.read())

# Update (append) new data
with open(file_name, "a") as file:
  file.write("\nAdding some new content...\n")
  file.write("File updated successfully!\n")

print("\n✅ File updated successfully!")

# Read again to confirm update
with open(file_name, "r") as file:
  print("\n--- Updated File Content ---")
  print(file.read())
