import sqlite3 as sql 
country = "Algeria".capitalize()


# file = open(country, 'r')
# lines = file.readlines()
conn = sql.connect(f'{country}.db')
cursor = conn.cursor()

# cursor.execute(f"Create table {country} (PhoneNumber INT PRIMARY KEY);")
query = f"SELECT * FROM {country};"
cursor.execute(query)
res = cursor.fetchall()
print(res)
# for line in lines:
#     number = line.split(',')[1]
#     print(f'Number => {number}')
#     if number.isnumeric():
#         cursor.execute(f'INSERT INTO {country} values({number})')
# conn.commit()
conn.close()


# db name -> Country 
# table -> Country 
# PhoneNumber 