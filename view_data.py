import sqlite3

# Connect to the database
conn = sqlite3.connect('predictions_1.db')
cursor = conn.cursor()

# Query the data from the correct table
cursor.execute('SELECT * FROM predictions')
rows = cursor.fetchall()

# Dynamically fetch column names
column_names = [description[0] for description in cursor.description]

# Function to convert values to their original form
def convert_value(column, value):
    if column == "brand":
        brands = {1.0: "Lenovo", 2.0: "Dell", 3.0: "HP", 4.0: "Asus", 5.0: "Acer", 6.0: "MSI", 7.0: "Toshiba", 8.0: "Apple"}  # Example mapping
        return brands.get(value, "Unknown")
    elif column == "type":
        types = {1.0: "Notebook", 2.0: "Gaming", 3.0: "Ultrabook", 4.0: "2-in-1 Convertible"}  # Example mapping
        return types.get(value, "Unknown")
    elif column == "touchscreen":
        return "Yes" if value == 1 else "No"
    elif column == "ips":
        return "Yes" if value == 1 else "No"
    elif column == "cpu_brand":
        cpu_brands = {1.0: "Intel Core i7", 2.0: "Intel Core i5", 3.0: "Intel Core i3", 4.0: "Other Intel Processor", 5.0: "AMD Processor"}  # Example mapping
        return cpu_brands.get(value, "Unknown")
    elif column == "gpu":
        gpus = {1.0: "Intel", 2.0: "NVIDIA", 3.0: "AMD"}  # Example mapping
        return gpus.get(value, "Unknown")
    elif column == "os":
        oss = {1.0: "Windows", 2.0: "Mac", 3.0: "No OS/Linux/Android/Chrome OS"}  # Example mapping
        return oss.get(value, "Unknown")
    else:
        return value

# Print the data with column headers
header = " ".join(f"{name:<15}" for name in column_names)
print(header)
print("=" * len(header))

# Print each row
for row in rows:
    row_data = " ".join(f"{str(convert_value(column_names[i], item)):<15}" for i, item in enumerate(row))
    print(row_data)

# Close the connection
conn.close()