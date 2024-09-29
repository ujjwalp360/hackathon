# db.py
import mysql.connector

# MySQL Database connection
def create_db_connection():
    return mysql.connector.connect(
        host="ber9n6myvypxkq2zmnmt-mysql.services.clever-cloud.com",          # Ensure this is your correct host
        user="ugrgq84wv7mb6riy",      # Correct username here
        password="ubd29UcTDrAGhd4nvuhX",  # Correct password here
        database="ber9n6myvypxkq2zmnmt"  # Correct database name
    )

