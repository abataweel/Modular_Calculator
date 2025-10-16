"""
History structure:
date/time / module / function / input / result
"""

import os
import sys
import csv
from datetime import datetime

# Find the folder of the exe or script
if getattr(sys, 'frozen', False):  # running as .exe
    base_folder = os.path.dirname(sys.executable)
else:  # running as .py
    base_folder = os.path.dirname(os.path.abspath(__file__))

# Path to CSV inside src/utils
FOLDER = os.path.join(base_folder, "src", "utils")
os.makedirs(FOLDER, exist_ok=True)  # create folder if missing

FILENAME = os.path.join(FOLDER, "history.csv")

def logCalc(module, function, input, result):
    try:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_exists = os.path.exists(FILENAME)
        with open(FILENAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Date", "Module", "Function", "Input", "Result"])
            writer.writerow([date, str(module), str(function), input, result])
    except PermissionError:
        print("No permission for writing, please close the excel file")
    except FileNotFoundError:
        print("Error: History file not found, new file created...")
