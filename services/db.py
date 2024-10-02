import mysql.connector

try:
  mydb = mysql.connector.connect(
    host="your_host_name", 
    user="your_username", 
    password="your_password" ,
    database="users"
  )
except:
    print(f"Connection error!!! Detail: {mysql.connector.Error}")