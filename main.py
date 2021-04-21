import sqlite3

connection = sqlite3.connect('census.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS density(province_or_territory TEXT, population INTEGER,land_area REAL)")

# cursor.execute("INSERT INTO density VALUES('Newfoundland and Labrador', 512930, 370501.69)")
# cursor.execute("INSERT INTO density VALUES('Prince Edward Island', 135294, 5684.39)")
# cursor.execute("INSERT INTO density VALUES('Nova Scotia', 908007, 52917.43)")
# cursor.execute("INSERT INTO density VALUES('New Brunswick', 729498, 71355.67)")
# cursor.execute("INSERT INTO density VALUES('Quebec', 7237479, 1357743.08)")
# cursor.execute("INSERT INTO density VALUES('Manitoba', 1119583, 551937.87)")
# cursor.execute("INSERT INTO density VALUES('Saskatchewan', 978933, 586561.35)")
# cursor.execute("INSERT INTO density VALUES('Alberta', 2974807, 639987.12)")
# cursor.execute("INSERT INTO density VALUES('British Columbia', 3907738, 926492.48)")
# cursor.execute("INSERT INTO density VALUES('Yukon Territory', 28674, 474706.97)")
# cursor.execute("INSERT INTO density VALUES('Northwest Territories', 37360, 1141108.37)")
# cursor.execute("INSERT INTO density VALUES('Nunavut', 26745, 1925460.18)")
#
# connection.commit()

cursor.execute('SELECT province_or_territory, population, land_area '
               'FROM density')
for row in cursor.fetchall():
    print(row)

print("============================================================")
print("============================================================")

cursor.execute('SELECT population '
               'FROM density')
for row in cursor.fetchall():
    print(row)

print("============================================================")
print("============================================================")

cursor.execute('SELECT province_or_territory, population, land_area '
               'FROM density '
               'WHERE population < 1000000')
for row in cursor.fetchall():
    print(row)

print("============================================================")
print("============================================================")

cursor.execute('SELECT province_or_territory, population, land_area '
               'FROM density '
               'WHERE population < 1000000 AND population > 5000000')
for row in cursor.fetchall():
    print(row)

print("============================================================")
print("============================================================")

cursor.execute('SELECT province_or_territory, population, land_area '
               'FROM density '
               'WHERE NOT population < 1000000 AND NOT population > 5000000')
for row in cursor.fetchall():
    print(row)

print("============================================================")
print("============================================================")

cursor.execute('SELECT population '
               'FROM density '
               'WHERE land_area > 200000')
for row in cursor.fetchall():
    print(row)

print("============================================================")
print("============================================================")

cursor.execute('SELECT province_or_territory, population/land_area AS population_density '
               'FROM density')
for row in cursor.fetchall():
    print(row)

connection.close()







