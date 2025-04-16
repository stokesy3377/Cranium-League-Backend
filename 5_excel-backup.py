import os 
import shutil
from datetime import datetime

# Step 1: Ask match info
match_count = input("How many matches were there today? (1 or 2): ").strip()

if match_count not in ['1', '2']:
    print("❌ Invalid input. Only '1' or '2' accepted.")
    exit()

# Step 2: Generate filename
today_str = datetime.now().strftime("%Y-%m-%d")

if match_count == '1':
    filename = f"{today_str}-CL_S1.xlsx"
elif match_count == '2':
    match_number = input("Was this the first or second match? (type 'first' or 'second'): ").strip().lower()
    if match_number not in ['first', 'second']:
        print("❌ Invalid input. Only 'first' or 'second' accepted.")
        exit()
    filename = f"{today_str}-CL_S1-{match_number}-match.xlsx"

# Step 3: Define existing backup folder path
backup_folder = "backup"  # Make sure this folder exists beforehand

# Step 4: Copy file
source_file = "CL_S1.xlsx"
destination_file = os.path.join(backup_folder, filename)

shutil.copy2(source_file, destination_file)

print(f"✅ Backup saved as: {destination_file}")
