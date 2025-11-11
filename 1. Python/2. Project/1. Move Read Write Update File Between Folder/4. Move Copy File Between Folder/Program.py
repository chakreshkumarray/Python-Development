
import os
import shutil

source_folder = r"E:\Python-Development\1. Python\2. Project\1. Move Read Write Update File Between Folder\1. Source File"
destination_folder = r"E:\Python-Development\1. Python\2. Project\1. Move Read Write Update File Between Folder\2. Destination File"
file_name = "students_data_marks.csv"

# build full path
source_path = os.path.join(source_folder, file_name)
destination_path = os.path.join(destination_folder, file_name)

# Check multiple conditions
if not os.path.exists(source_path):
  print("❌ Source file not found!")

elif not os.path.isdir(source_folder):
  print("❌ Source folder does not exist!")

elif not os.path.isdir(destination_folder):
  print("⚠️ Destination folder not found! Creating it...")
  os.makedirs(destination_folder, exist_ok=True)
  shutil.copy(source_path, destination_path)
  print(f"{file_name} ✅ File copied successfully after creating destination folder!")

elif os.path.exists(destination_path):
  print("⚠️ File already exists in destination folder!")

else:
  shutil.copy(source_path, destination_path)
  print(f"{file_name} ✅ File copied successfully!")    
