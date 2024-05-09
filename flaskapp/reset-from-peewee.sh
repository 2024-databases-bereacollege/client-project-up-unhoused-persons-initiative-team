# Remove objects from the database
psql -c  "DROP TABLE IF EXISTS Inventory_Usage CASCADE;"
psql -c  "DROP TABLE IF EXISTS Inventory CASCADE;"
psql -c  "DROP TABLE IF EXISTS Volunteer CASCADE;"
psql -c  "DROP TABLE IF EXISTS Visit_Service CASCADE;"
psql -c  "DROP TABLE IF EXISTS Visit_Record CASCADE;"
psql -c  "DROP TABLE IF EXISTS Neighbor CASCADE;"
psql -c  "DROP TABLE IF EXISTS Services CASCADE;"
psql -c  "DROP TABLE IF EXISTS Service_Providers CASCADE;"  
psql -c  "DROP TABLE IF EXISTS migratehistory;"  

# Cleaning up any existing migration files
rm -rf migrations
rm -f migrations.json

# Initialize peewee-migrate if not already initialized
pem init

# Use peewee-migrate to create tables from Peewee models
pem add models.Service_Providers
pem add models.Services
pem add models.Volunteer
pem add models.Neighbor
pem add models.Visit_Record
pem add models.Visit_Service
pem add models.Inventory_Usage
pem add models.Inventory

# Apply migrations to create tables based on models
pem watch
pem migrate

# Populate database with test data
#python populate_data.py  # Run data population script #Commenting this out because this is a broken file -NH

python sample_data.py
