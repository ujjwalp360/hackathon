# db.py
import mysql.connector

# MySQL Database connection
def create_db_connection():
    return mysql.connector.connect(
        host="ber9n6myvypxkq2zmnmt-mysql.services.clever-cloud.com",
        user="ubd29UcTDrAGhd4nvuhX",
        database="ber9n6myvypxkq2zmnmt"
    )
