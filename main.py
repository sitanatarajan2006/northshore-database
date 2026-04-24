from database import (
    shipments_table,
    drivers_table,
    vehicles_table,
    warehouse_table,
    inventory_table
)

# Create all system tables
shipments_table()
drivers_table()
vehicles_table()
warehouse_table()
inventory_table()

print("All database tables created successfully!")