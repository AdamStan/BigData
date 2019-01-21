import csv

old_file = 'IDSData.csv'

new_file = 'IDS/data.csv'

i = 0

add_to_buff = [
    "Average grace period on new external debt commitments (years)",
    "Commitments official creditors (COM current US$)",
    r"Concessional debt (% of total external debt)",
    "Debt stock reduction (current US$)",
    "External debt stocks total (DOD current US$)",
    "Interest payments on external debt total (INT current US$)",
    r"Short-term debt (% of total external debt)",
    "Technical cooperation grants (current US$)",
]

content = []

# otwieramy plik z ktorego bierzemy dane

with open(old_file, 'r', newline='') as csv_file_read:
    reader = csv.reader(csv_file_read)

    buff_row = []
    next(reader)
    for row in reader:
			
        buff_row = []
        for i in range(0, 2):
            buff_row.append(row[i])

        string = row[2].replace(',',' ')
        string = string.replace("  "," ")

        if string in add_to_buff:
            buff_row.append(string)
        else:
            continue
        
        buff_row.append(row[3])
        
        for i in range(40, 50):
            if row[i]:
                buff_row.append(row[i])
            else:
                buff_row.append(0)

        content.append(buff_row)

    # dane zapisujemy do nowej csvki
    with open(new_file, 'w', newline='') as csv_file_write:
        writer = csv.writer(csv_file_write)
        for row in content:
            writer.writerow(row)
			
