import sqlite3
from importlib_metadata import NullFinder
import pandas as pd
import requests
from sqlalchemy import null
import os

"""def tries():
    test_file = open("contact.csv", "rb")
    test_url = "http://127.0.0.1:5000/send"
    test_response = requests.post(test_url, files = {"form_field_name": test_file})
    if test_response.ok:
        print("Upload completed successfully!")
        print(test_response.text)
    else:
        print("Something went wrong!")
tries()
sqliteConnection = sqlite3.connect('Data.db')
cursor = sqliteConnection.cursor() 
print("Connected to SQLite")
 
EMAIL_ADDRESS = cursor.execute("select email from sender where username = '{}'".format('hiba')).fetchall()
print(EMAIL_ADDRESS[0][0])


cursor.close()

sqliteConnection = sqlite3.connect('Data.db')
cursor = sqliteConnection.cursor() 
print("Connected to SQLite")
contact_file2 = pd.read_csv('contact.csv')
for i in range(len(contact_file2)):
    cursor.execute("INSERT INTO contacts (`contact-name`, email)VALUES ('{}','{}');".format(contact_file2['NAME'][i],contact_file2['EMAILS'][i]))
    sqliteConnection.commit()
cursor.close()

from cryptography.fernet import Fernet
def write_key():
    
    #Generates a key and save it into a file
    
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    
   # Loads the key from the current directory named `key.key`
    
    return open("key.key", "rb").read()

write_key()
key = load_key()

message = "some secret message".encode()
# initialize the Fernet class
f = Fernet(key)
# encrypt the message
encrypted = f.encrypt(message)
print(encrypted)
decrypted_encrypted = f.decrypt(encrypted)
print(decrypted_encrypted)
"""
sqliteConnection = sqlite3.connect('Data.db')
cursor = sqliteConnection.cursor() 
print("Connected to SQLite")
#sender = cursor.execute("SELECT * FROM sender where email = '{}';".format(proj_sender_email)).fetchall()
project = cursor.execute("SELECT * FROM project;").fetchall()
content = cursor.execute("SELECT * FROM content;").fetchall()
#print(sender,project)
proj_name = []
proj_sender_email = []
proj_sender_username = []
proj_date = []
proj_status = []
proj_num = []
for i in range(len(project)):
    proj_num.append(i)
    proj_name.append(project[i][1])
    #proj_sender_username.append(project[i][1])
    proj_sender_email.append(project[i][3])
    sender = cursor.execute("SELECT username FROM sender where email = '{}';".format(proj_sender_email[i])).fetchall()
    proj_sender_username.append(sender[0][0])
    proj_date.append(project[i][2])
    proj_status.append(project[i][4])
print(proj_sender_email,proj_name,proj_status,proj_date,proj_sender_username )
