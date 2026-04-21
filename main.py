from database import create_shipments_table, create_drivers_table, create_vehicles_table

# Run database setup step-by-step
create_shipments_table()
create_drivers_table()
create_vehicles_table()

print("Core tables created successfully!")