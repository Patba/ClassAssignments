import csv


with open("firma.csv", encoding="utf-8") as pc:
    csv_reader = csv.reader(pc, delimiter=";")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'tytuly kolumn: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} pracuje na stanowisku: {row[1]} i ma urodziny w miesiącu: {row[2]},'
                  f'otrzymuje nagrodę w wysokości {row[3]} zł')
            line_count += 1
    print(f'wczytano {line_count} wierszy')
    print(f'wczytano {line_count-1} osób')