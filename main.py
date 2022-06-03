import sqlite3, csv


sqlite_con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) # change to 'sqlite:///your_filename.db'
# This little bugger above https://stackoverflow.com/questions/1829872/how-to-read-datetime-back-from-sqlite-as-a-datetime-instead-of-string-in-python
cur = sqlite_con.cursor()

#Tworzymy pusta tabele polaczenia
cur.execute('''CREATE TABLE polaczenia (from_subscriber data_type INTEGER, 
                  to_subscriber data_type INTEGER, 
                  datetime data_type timestamp, 
                  duration data_type INTEGER , 
                  celltower data_type INTEGER);''') # use your column names here

#Otwieramy plik.csv i przerzucamy go w najprostszy sposób do naszej nowo utworzonej bazy sqlite
with open('polaczenia_duze.csv','r') as fin: 
    # csv.DictReader uses first line in file for column headings by default
    reader = csv.reader(fin, delimiter = ";") # comma is default delimiter
    next(reader, None)  # skip the headers
    rows = [x for x in reader]
    cur.executemany("INSERT INTO polaczenia (from_subscriber, to_subscriber, datetime, duration , celltower) VALUES (?, ?, ?, ?, ?);", rows)
    sqlite_con.commit()

cursor = sqlite_con.cursor()
cursor.execute("Select sum(duration) from polaczenia")
result = cursor.fetchone()[0]
result

if __name__ == '__main__':
    print (result)

