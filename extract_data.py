import csv

old_file = 'IDSData.csv'

new_file = 'IDS/data.csv'

i = 0

content = []

# otwieramy plik z ktorego bierzemy dane

with open(old_file, 'r', newline='') as csv_file_read:
    reader = csv.reader(csv_file_read)

    buff_row = []
    next(reader)
    for row in reader:
        i += 1
        if i % 3 != 1:
            continue
			
        buff_row = []
        for i in range(0, 4):
            if i >= 2:
                string = row[i].replace(',',' ')
                buff_row.append(string)
            else:
                buff_row.append(row[i])

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
			
