# Remove objects from the database
# psql -c "DROP table IF EXISTS example;"
# psql -c "DROP table IF EXISTS othertable;"
# psql -c "DROP table IF EXISTS Visit_Record;"
# psql -c "DROP table IF EXISTS Visit_Service;"
psql -c "DROP TABLE IF EXISTS Visit_Record;"
psql -c "DROP TABLE IF EXISTS Visit_Service;"
psql -c "DROP TABLE IF EXISTS Volunteer;"
psql -c "DROP TABLE IF EXISTS Neighbor;"
psql -c "DROP TABLE IF EXISTS Service_Providers;"
psql -c "DROP TABLE IF EXISTS Services;"
psql -c "DROP TABLE IF EXISTS Inventory;"

# Create tables
< tables.sql psql


# Load data back into database
< data.sql psql
