import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('database_1.db')
cursor = conn.cursor()

# Create the table for storing predictions
cursor.execute('''
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand REAL,
    type REAL,
    ram INTEGER,
    weight REAL,
    touchscreen INTEGER,
    ips INTEGER,
    cpu_brand REAL,
    ssd INTEGER,
    hdd INTEGER,
    gpu REAL,
    os REAL,
    prediction REAL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()