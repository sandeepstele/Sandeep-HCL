import mysql.connector
import csv
data=[]
filename = 'data.csv'

with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)
# Establish a connection to the MySQL server
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='tiger',
    database='dataset'
)
cursor = cnx.cursor()

# Create a table if it doesn't exist
create_table_query = '''
    CREATE TABLE IF NOT EXISTS your_table(
        Name VARCHAR(255),
        Address VARCHAR(255),
        ID VARCHAR(36) PRIMARY KEY,
        Skill VARCHAR(255),
        Region VARCHAR(255),
        Year VARCHAR(255),
        Technology VARCHAR(255)
    )
'''
cursor.execute(create_table_query)

# Insert data into the table or update existing rows
insert_query = '''
    INSERT INTO your_table (Name, Address, ID, Skill, Region, Year, Technology)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        Name = VALUES(Name),
        Address = VALUES(Address),
        Skill = VALUES(Skill),
        Region = VALUES(Region),
        Year = VALUES(Year),
        Technology = VALUES(Technology)
'''

for row in data:
    cursor.execute(insert_query, row)

# Commit the changes and close the connection
cnx.commit()
cursor.close()
cnx.close()
