"""history, structure may be like

-- date and time / module / specific calucaltion /  result


"""
import csv
import csv
import os
from datetime import datetime

FILENAME = "history.csv"


def logCalc(module,function,input,result):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(FILENAME)
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date","Module","function","input","result"])
        writer.writerow([date, module, function,input,result])
