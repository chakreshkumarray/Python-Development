
import csv
import os

file_name = "data.csv"

# Check if file exists
if not os.path.exists(file_name):
    # Create file and write initial 5x5 data
    with open(file_name, "w", newline="") as file:
      writer = csv.writer(file)
      writer.writerow(["ID", "Name", "Age", "City", "Score"])
      writer.writerow([1, "Alice", 23, "Delhi", 85])
      writer.writerow([2, "Bob", 27, "Mumbai", 90])
      writer.writerow([3, "Charlie", 22, "Bangalore", 75])
      writer.writerow([4, "Diana", 25, "Pune", 88])
      writer.writerow([5, "Ethan", 29, "Chennai", 92])
    print("🆕 File created and data written.")
else:
  print("📄 File already exists.")

# Read the file
print("\n--- Current CSV Content ---")
with open(file_name, "r") as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)

# Update (append) new data
with open(file_name, "a", newline="") as file:
  writer = csv.writer(file)
  writer.writerow([6, "Farhan", 24, "Kolkata", 81])
  writer.writerow([7, "Grace", 26, "Hyderabad", 89])

print("\n✅ File updated successfully!")

# ✅ Read again to confirm update
print("\n--- Updated CSV Content ---")
with open(file_name, "r") as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)
