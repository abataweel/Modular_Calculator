"""history, structure may be like

-- date and time / module / specific calucaltion / input /  result

"""
import csv
import os
from datetime import datetime

FILENAME = "./src/utils/history.csv"

def logCalc(module,function,input,result):
    try:
     FILENAME = os.path.join(os.path.dirname(__file__), "history.csv")

     date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     file_exists = os.path.exists(FILENAME)
     with open(FILENAME, mode="a", newline="") as file:
         writer = csv.writer(file)
         if not file_exists:
             writer = csv.writer(file)
             writer.writerow(["Date","Module","Function","input","result"])
         writer.writerow([date, str(module), str(function),input,result])
    except PermissionError:
        print("\033[91mNo permission for writing, please close the excel file\033[0m")
    except FileNotFoundError:
        print("\033[91mError:History file not found, new file created...\033[0m")
        
        
