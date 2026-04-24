import sqlite3
def connect():
    conn = sqlite3.connect("northshore.db") #creates the file if it does not exist
    return conn
#function to create shipment table only
def shipments_table():
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
# Create drivers table
def drivers_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS drivers (
        driver_id INTEGER PRIMARY KEY,
        name TEXT,
        license_number TEXT,
        phone TEXT
    )
    """)

    conn.commit()
    conn.close()


# Create vehicles table
def vehicles_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehicles (
        vehicle_id INTEGER PRIMARY KEY,
        vehicle_type TEXT,
        capacity INTEGER,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


#Create warehouse table
def warehouse_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS warehouses (
        warehouse_id INTEGER PRIMARY KEY,
        location TEXT,
        manager_name TEXT
    )
    """)

    conn.commit()
    conn.close()

# Create inventory table
def inventory_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        item_id INTEGER PRIMARY KEY,
        item_name TEXT,
        quantity INTEGER,
        warehouse_id INTEGER
    )
    """)

    conn.commit()
    conn.close()