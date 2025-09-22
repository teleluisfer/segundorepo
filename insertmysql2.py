import mysql.connector

# Connect to the MySQL server
db = mysql.connector.connect(
  host="10.221.93.147",
  user="root",
  password="lsuy0",
  database="orion"
)

# Create a cursor object
db = mysql.connector.connect(user='root', password='lsuy0', host='10.221.93.147', database='orion', auth_plugin='mysql_native_password')
cursor = db.cursor()


# Prepare the SQL query
sql = "INSERT INTO test1 (username, email) VALUES (%s, %s)"
values = ("John Smith", "123 Main St")


# Execute the query
cursor.execute(sql, values)

# Commit the changes
db.commit()

# Print the number of rows affected
print(cursor.rowcount, "record inserted.")
