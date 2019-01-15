import csv

file = open('IDSData.csv','r')
content = file.read()
content = content.replace(","," ")
rows_of_content = content.split("\n")
# print(content)
# print(rows_of_content)
new_file = 'IDS/data.csv'

with open(new_file,'w',newline='') as csv_file:
    writer = csv.writer(csv_file)
    header = rows_of_content[0]
    header = header.split()
    writer.writerow(header)
    rows_of_content.pop(0)
    i = 0

    for row in rows_of_content:
        buff = row.split()
        # print(row)
        i += 1
        if i % 3 != 1:
            continue

        # while(True):
        #    try:
        #        f = float(buff[1])
        #        break
        #    except Exception:
        #        buff[0] = buff[0] + " " + buff[1]
        #        buff.pop(1)
        writer.writerow(buff)
