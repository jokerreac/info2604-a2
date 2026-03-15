# STUDENT ID : 816041392

import csv, hashlib

print('[Dictionary Attack]')

# Load database CSV into memory
file_db = 'database.csv'
database = []

try:
    with open(file_db, 'r', encoding='utf-8') as file:
        csvreader = csv.DictReader(file)

        for row in csvreader:
            database.append(row)
    
    print(f'> Database loaded from {file_db}')

except FileNotFoundError:
    print('> Error: database.csv not found')

# Load dictionary and build rainbow table
file_dict = 'English.dic.txt'
rainbow_table = {}

try:
    with open(file_dict, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            hashed_word = hashlib.sha1(word.encode('utf-8')).hexdigest()
            rainbow_table[hashed_word] = word
    
    print(f'> Rainbow table built from {file_dict}\n')

except FileNotFoundError:
    print('> Error: English.dic.txt not found')

# Compare stored hashes against rainbow table
print('Recovering passwords ...')
recovered_count = 0

for record in database:
    stored_hash = record['list_password']

    if stored_hash in rainbow_table:
        record['list_password'] = rainbow_table[stored_hash]
        recovered_count += 1

        print(f"> Recovered :\t{record['id_num']:<12}{record['list_user']:<20}{record['list_password']}")

# Calculate recovery percentage
if len(database) > 0:
    recovered_percentage = (recovered_count / len(database)) * 100
    print(f'>> {recovered_percentage:.2f}% of records recovered!')

else:
    print('> No database records found')