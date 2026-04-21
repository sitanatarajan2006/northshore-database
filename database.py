import sqlite3
def connect():
    conn = sqlite3.connect("northshore.db") #creates the file if it does not exist
    return conn
#function to create shipment table only
def create_shipments_table():
    conn = connect()
    cursor = conn.cursor

    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipments (
        shipment_id INTEGER PRIMARY KEY,
        order_number TEXT,
        sender_name TEXT,
        receiver_name TEXT,
        delivery_status TEXT
    )
    """)

    conn.commit()
    conn.close()