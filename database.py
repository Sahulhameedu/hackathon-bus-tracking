import sqlite3

conn = sqlite3.connect('bus.db')

c =conn.cursor()

# c.execute("""CREATE TABLE buses(
#           bus_number integer,
#           driver_name text, 
#           from_location text, 
#           to_location text, 
#           registration_number text
# )""")
c.execute("INSERT INTO buses VALUES(1,'Arul','Ayyalur','Natham','TN 57 BT 1234')")
# c.execute("DELETE from buses WHERE bus_number=1")
c.execute("SELECT * FROM buses")
print(c.fetchall())
conn.commit()
conn.close()