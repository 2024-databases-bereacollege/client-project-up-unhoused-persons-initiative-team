from datetime import datetime
from models import *
from peewee import *
db = PostgresqlDatabase("postgres", host="localhost", user="postgres", password="postgres")

def generate_sample_data():
    # Sample data for Service_Providers table
    def service_providers_sample_data():
        return [
            {
                'Organization_Name': 'ABC Services',
                'ContactPerson': 'John Doe',
                'Email': 'john@abcservices.com',
                'Phone': '123-456-7890',
                'DateOfStart': '2022-01-01'
            },
            {
                'Organization_Name': 'XYZ Solutions',
                'ContactPerson': 'Jane Smith',
                'Email': 'jane@xyzsolutions.com',
                'Phone': '987-654-3210',
                'DateOfStart': '2021-05-15'
            },
            {
                'Organization_Name': 'PQR Foundation',
                'ContactPerson': 'Mike Johnson',
                'Email': 'mike@pqrfoundation.org',
                'Phone': '555-123-4567',
                'DateOfStart': '2023-02-28'
            },
            {
                'Organization_Name': 'LMN Assistance',
                'ContactPerson': 'Sarah Brown',
                'Email': 'sarah@lmnassistance.com',
                'Phone': '111-222-3333',
                'DateOfStart': '2020-11-10'
            },
            {
                'Organization_Name': 'EFG Support',
                'ContactPerson': 'David Wilson',
                'Email': 'david@efgsupport.org',
                'Phone': '444-555-6666',
                'DateOfStart': '2022-09-01'
            }
        ]

    # Sample data for Services table
    def services_sample_data():
        return [
            {
                'ServiceType': 'Cleaning',
                'OrganizationID': 1
            },
            {
                'ServiceType': 'Food Delivery',
                'OrganizationID': 2
            },
            {
                'ServiceType': 'Clothing Donation',
                'OrganizationID': 3
            },
            {
                'ServiceType': 'Medical Assistance',
                'OrganizationID': 4
            },
            {
                'ServiceType': 'Job Training',
                'OrganizationID': 5
            }
        ]

    # Sample data for Volunteer table
    def volunteers_sample_data():
        return [
            {
                'FirstName': 'Alice',
                'LastName': 'Smith',
                'Password': 'password123',
                'Email': 'alice@example.com',
                'Phone': '987-654-3210',
                'HasRecordAccess': True
            },
            {
                'FirstName': 'Bob',
                'LastName': 'Johnson',
                'Password': 'qwerty456',
                'Email': 'bob@example.com',
                'Phone': '111-222-3333',
                'HasRecordAccess': False
            },
            {
                'FirstName': 'Emily',
                'LastName': 'Davis',
                'Password': 'pass1234',
                'Email': 'emily@example.com',
                'Phone': '444-555-6666',
                'HasRecordAccess': True
            },
            {
                'FirstName': 'Michael',
                'LastName': 'Wilson',
                'Password': 'abcd1234',
                'Email': 'michael@example.com',
                'Phone': '777-888-9999',
                'HasRecordAccess': False
            },
            {
                'FirstName': 'Sarah',
                'LastName': 'Brown',
                'Password': 'password789',
                'Email': 'sarah@example.com',
                'Phone': '555-666-7777',
                'HasRecordAccess': True
            }
        ]

# Sample data for Neighbor table
    def neighbors_sample_data():
        return [
            {
                'VolunteerID': 1,
                'OrganizationID': 1,
                'FirstName': 'Bob',
                'LastName': 'Johnson',
                'DateOfBirth': '1990-05-15',
                'Phone': '555-123-4567',
                'Location': '123 Main St',
                'Email': 'bob@example.com',
                'HasStateID': True,
                'HasPet': False
            },
            {
                'VolunteerID': 2,
                'OrganizationID': 2,
                'FirstName': 'Emily',
                'LastName': 'Davis',
                'DateOfBirth': '1985-09-20',
                'Phone': '111-222-3333',
                'Location': '456 Elm St',
                'Email': 'emily@example.com',
                'HasStateID': False,
                'HasPet': True
            },
            {
                'VolunteerID': 3,
                'OrganizationID': 3,
                'FirstName': 'Michael',
                'LastName': 'Wilson',
                'DateOfBirth': '1978-02-10',
                'Phone': '444-555-6666',
                'Location': '789 Oak Ave',
                'Email': 'michael@example.com',
                'HasStateID': True,
                'HasPet': False
            },
            {
                'VolunteerID': 4,
                'OrganizationID': 4,
                'FirstName': 'Sarah',
                'LastName': 'Brown',
                'DateOfBirth': '1995-12-03',
                'Phone': '777-888-9999',
                'Location': '321 Pine Rd',
                'Email': 'sarah@example.com',
                'HasStateID': True,
                'HasPet': True
            },
            {
                'VolunteerID': 5,
                'OrganizationID': 5,
                'FirstName': 'David',
                'LastName': 'Taylor',
                'DateOfBirth': '1982-07-25',
                'Phone': '222-333-4444',
                'Location': '654 Cedar Ln',
                'Email': 'david@example.com',
                'HasStateID': False,
                'HasPet': False
            }
        ]

    # Sample data for Visit_Service table
    def visit_services_sample_data():
        return [
            {
                'ServiceID': 1,
                'Description': 'Weekly cleaning service',
                'Date': '2023-06-01'
            },
            {
                'ServiceID': 2,
                'Description': 'Monthly food delivery',
                'Date': '2023-07-15'
            },
            {
                'ServiceID': 3,
                'Description': 'Clothing donation drive',
                'Date': '2023-08-10'
            },
            {
                'ServiceID': 4,
                'Description': 'Medical check-up and consultation',
                'Date': '2023-09-05'
            },
            {
                'ServiceID': 5,
                'Description': 'Job training workshop',
                'Date': '2023-10-20'
            }
        ]

# Sample data for Visit_Record table
    def visit_records_sample_data():
        return [
            {'NeighborID': 1, 'VolunteerID': 1, 'RecordID': 1},
            {'NeighborID': 2, 'VolunteerID': 2, 'RecordID': 2},
            {'NeighborID': 3, 'VolunteerID': 3, 'RecordID': 3},
            {'NeighborID': 4, 'VolunteerID': 4, 'RecordID': 4},
            {'NeighborID': 5, 'VolunteerID': 5, 'RecordID': 5}
        ]

# Sample data for Inventory_Usage table
    def inventory_usage_sample_data():
        return [
            {
                'NameOfItem': 'Cleaning Supplies',
                'RecordID': 1,
                'Description_of_Item': 'Mop and bucket',
                'Number_Of_Item_Used': 1
            },
            {
                'NameOfItem': 'Food Items',
                'RecordID': 2,
                'Description_of_Item': 'Canned goods',
                'Number_Of_Item_Used': 10
            },
            {
                'NameOfItem': 'Clothing',
                'RecordID': 3,
                'Description_of_Item': 'T-shirts and jeans',
                'Number_Of_Item_Used': 5
            },
            {
                'NameOfItem': 'Medical Supplies',
                'RecordID': 4,
                'Description_of_Item': 'Bandages and antiseptic',
                'Number_Of_Item_Used': 3
            },
            {
                'NameOfItem': 'Stationery',
                'RecordID': 5,
                'Description_of_Item': 'Pens and notebooks',
                'Number_Of_Item_Used': 8
            }
        ]

    # Sample data for Inventory table
    def inventory_sample_data():
        return [
            {
                'NameOfItem': 'Cleaning Supplies',
                'VolunteerID': 1,
                'Description_of_Item': 'Mop and bucket',
                'ExpirationDate': '2024-12-31',
                'Number_Of_Item': 10
            },
            {
                'NameOfItem': 'Food Items',
                'VolunteerID': 2,
                'Description_of_Item': 'Canned goods',
                'ExpirationDate': '2023-09-30',
                'Number_Of_Item': 50
            },
            {
                'NameOfItem': 'Clothing',
                'VolunteerID': 3,
                'Description_of_Item': 'T-shirts and jeans',
                'ExpirationDate': '2023-09-30', #TODO listed as cannot be NULL?
                'Number_Of_Item': 20
            },
            {
                'NameOfItem': 'Medical Supplies',
                'VolunteerID': 4,
                'Description_of_Item': 'Bandages and antiseptic',
                'ExpirationDate': '2025-06-30',
                'Number_Of_Item': 15
            },
            {
                'NameOfItem': 'Stationery',
                'VolunteerID': 5,
                'Description_of_Item': 'Pens and notebooks',
                'ExpirationDate': '2025-06-30',
                'Number_Of_Item': 30
            }
        ]

    return {
        'service_providers': service_providers_sample_data(),
        'services': services_sample_data(),
        'volunteers': volunteers_sample_data(),
        'neighbors': neighbors_sample_data(),
        'visit_services': visit_services_sample_data(),
        'visit_records': visit_records_sample_data(),
        'inventory_usage': inventory_usage_sample_data(),
        'inventory': inventory_sample_data()
    }


if __name__ == '__main__':
    # Connect to the PostgreSQL database
    db.connect()

    # Generate and insert the sample data
    sample_data = generate_sample_data()
    with db.atomic():
        Service_Providers.insert_many(sample_data['service_providers']).execute()
        Services.insert_many(sample_data['services']).execute()
        Volunteer.insert_many(sample_data['volunteers']).execute()
        Neighbor.insert_many(sample_data['neighbors']).execute()
        Visit_Service.insert_many(sample_data['visit_services']).execute()
        Visit_Record.insert_many(sample_data['visit_records']).execute()
        Inventory_Usage.insert_many(sample_data['inventory_usage']).execute()
        Inventory.insert_many(sample_data['inventory']).execute()

    # Close the database connection
    db.close()

# def generate_sample_data():
#     service_providers_sample_data = [
#         {"Organization_Name": "Springfield Shelter", "ContactPerson": "David Green", "Email": "contact@springfieldshelter.org", "Phone": "555-0301", "DateOfStart": datetime.date(2000, 1, 1)},
#         {"Organization_Name": "Food Bank of Springfield", "ContactPerson": "Eva Turner", "Email": "info@foodbankspringfield.org", "Phone": "555-0302", "DateOfStart": datetime.date(2005, 6, 15)},
#         {"Organization_Name": "Springfield Elderly Care", "ContactPerson": "Franklin Moore", "Email": "care@springfieldelderly.org", "Phone": "555-0303", "DateOfStart": datetime.date(2010, 9, 20)},
#         {"Organization_Name": "Health Clinic", "ContactPerson": "Sara Miles", "Email": "contact@healthclinic.org", "Phone": "555-0304", "DateOfStart": datetime.date(2012, 3, 17)},
#         {"Organization_Name": "Youth Center", "ContactPerson": "Brian Clark", "Email": "info@youthcenter.org", "Phone": "555-0305", "DateOfStart": datetime.date(2015, 7, 10)}
#     ]

#     volunteers_sample_data = [
#         {"FirstName": "John", "LastName": "Doe", "Password": "hashed_password1", "Email": "john.doe@example.com", "Phone": "555-0101", "HasRecordAccess": True},
#         {"FirstName": "Jane", "LastName": "Smith", "Password": "hashed_password2", "Email": "jane.smith@example.com", "Phone": "555-0102", "HasRecordAccess": False},
#         {"FirstName": "Emily", "LastName": "Jones", "Password": "hashed_password3", "Email": "emily.jones@example.com", "Phone": "555-0103", "HasRecordAccess": True},
#         {"FirstName": "Michael", "LastName": "Brown", "Password": "hashed_password4", "Email": "michael.brown@example.com", "Phone": "555-0104", "HasRecordAccess": False},
#         {"FirstName": "Jessica", "LastName": "Davis", "Password": "hashed_password5", "Email": "jessica.davis@example.com", "Phone": "555-0105", "HasRecordAccess": True},
#         {"FirstName": "Daniel", "LastName": "Miller", "Password": "hashed_password6", "Email": "daniel.miller@example.com", "Phone": "555-0106", "HasRecordAccess": False},
#         {"FirstName": "Laura", "LastName": "Wilson", "Password": "hashed_password7", "Email": "laura.wilson@example.com", "Phone": "555-0107", "HasRecordAccess": True},
#         {"FirstName": "Robert", "LastName": "Moore", "Password": "hashed_password8", "Email": "robert.moore@example.com", "Phone": "555-0108", "HasRecordAccess": False},
#         {"FirstName": "Linda", "LastName": "Taylor", "Password": "hashed_password9", "Email": "linda.taylor@example.com", "Phone": "555-0109", "HasRecordAccess": True},
#         {"FirstName": "William", "LastName": "Anderson", "Password": "hashed_password10", "Email": "william.anderson@example.com", "Phone": "555-0110", "HasRecordAccess": False}
#     ]
    
# def insert_services():
#         services_sample_data = Service_Providers.select()
#         services_sample_data = [
#         {"ServiceType": "Meal Delivery", "OrganizationID": Service_Providers[0].id},
#         {"ServiceType": "Legal Aid", "OrganizationID": Service_Providers[1].id},
#         {"ServiceType": "Home Repairs", "OrganizationID": Service_Providers[2].id},
#         {"ServiceType": "Medical Checkup", "OrganizationID": Service_Providers[3].id},
#         {"ServiceType": "Youth Mentoring", "OrganizationID": Service_Providers[4].id}
#     ]

# def insert_neighbors():
#     volunteers = Volunteer.select()
#     service_providers = Service_Providers.select()
#     neighbors_sample_data = [
#         {"FirstName": "Alice", "LastName": "Johnson", "VolunteerID": volunteers[0].id, "OrganizationID": service_providers[0].id, "DateOfBirth": datetime.date(1980, 5, 15), "Phone": "555-0201", "Location": "123 Elm Street, Springfield", "Email": "alice.j@example.com", "Created_date": datetime.datetime.now(), "HasStateID": True, "HasPet": False},
#         {"FirstName": "Bob", "LastName": "Smith", "VolunteerID": volunteers[1].id, "OrganizationID": service_providers[1].id, "DateOfBirth": datetime.date(1975, 8, 25), "Phone": "555-0202", "Location": "456 Maple Avenue, Springfield", "Email": "bob.s@example.com", "Created_date": datetime.datetime.now(), "HasStateID": False, "HasPet": True},
#         {"FirstName": "Catherine", "LastName": "Williams", "VolunteerID": volunteers[2].id, "OrganizationID": service_providers[2].id, "DateOfBirth": datetime.date(1992, 11, 30), "Phone": "555-0203", "Location": "789 Pine Road, Springfield", "Email": "catherine.w@example.com", "Created_date": datetime.datetime.now(), "HasStateID": True, "HasPet": True}
#     ]
# def insert_visit_service():
#     service_types = ServiceType.select()
#     visit_services_sample_data = [
#         {
#             "ServiceType": service_types[0].id,
#             "Organization": "Food Bank of Springfield",
#             "ServiceType": "Meal Delivery",
#             "Description": "Delivered weekly meals to the individual."
#         },
#         {
#             "ServiceType": service_types[1].id,
#             "Organization": "Springfield Shelter",
#             "ServiceType": "Legal Aid",
#             "Description": "Provided legal consultation for housing rights."
#         },
#         {
#             "ServiceType": service_types[2].id,
#             "Organization": "Springfield Elderly Care",
#             "ServiceType": "Home Repairs",
#             "Description": "Assisted in minor home repairs to improve safety."
#         }
#     ]




# def insert_visit_records():
#     neighbors = Neighbor.select()
#     volunteers = Volunteer.select()
#     visit_service = Visit_Service.select()  # Assuming Visit_Service is the correct table name
#     visit_records_sample_data = [
#         {"NeighborID": neighbors[0].id, "VolunteerID": volunteers[0].id, "Date": datetime.date(2023, 10, 1)},
#         {"NeighborID": neighbors[0].id, "VolunteerID": volunteers[1].id, "Date": datetime.date(2023, 10, 3)},
#         {"NeighborID": neighbors[0].id, "VolunteerID": volunteers[2].id, "Date": datetime.date(2023, 10, 5)}
#     ]

# def insert_inventory_records():
#     volunteers = Volunteer.select()
#     inventory_sample_data = [
#         {"InventoryID": 1, "NameOfItem": "Canned Beans", "VolunteerID": volunteers[0].id, "Description_of_Item": "Food item", "ExpirationDate": datetime.date(2025, 12, 31), "Number_Of_Item": 100},
#         {"InventoryID": 2, "NameOfItem": "Winter Coats", "VolunteerID": volunteers[1].id, "Description_of_Item": "Clothing item", "ExpirationDate": datetime.date(2024, 11, 30), "Number_Of_Item": 40},
#         {"InventoryID": 3, "NameOfItem": "School Supplies", "VolunteerID": volunteers[2].id, "Description_of_Item": "Educational item", "ExpirationDate": datetime.date(2023, 8, 31), "Number_Of_Item": 200},
#         {"InventoryID": 4, "NameOfItem": "First Aid Kits", "VolunteerID": volunteers[3].id, "Description_of_Item": "Medical item", "ExpirationDate": datetime.date(2025, 1, 15), "Number_Of_Item": 50},
#         {"InventoryID": 5, "NameOfItem": "Flashlights", "VolunteerID": volunteers[4].id, "Description_of_Item": "Utility item", "ExpirationDate": datetime.date(2026, 7, 20), "Number_Of_Item": 75}
#     ]

# def insert_inventory_usage_records():
#     inventory_records = Inventory.select()
#     inventory_usage_sample_data = [
#         {"Inventory_UseID": 1, "InventoryID": inventory_records[0].id, "Description_of_Item": "Used for meal preparation", "Number_Of_Item_Used": 10},
#         {"Inventory_UseID": 2, "InventoryID": inventory_records[1].id, "Description_of_Item": "Distributed to individuals in need", "Number_Of_Item_Used": 5},
#         {"Inventory_UseID": 3, "InventoryID": inventory_records[2].id, "Description_of_Item": "Provided to families for educational support", "Number_Of_Item_Used": 25},
#         {"Inventory_UseID": 4, "InventoryID": inventory_records[3].id, "Description_of_Item": "Used in health and safety training sessions", "Number_Of_Item_Used": 3},
#         {"Inventory_UseID": 5, "InventoryID": inventory_records[4].id, "Description_of_Item": "Given for emergency preparedness", "Number_Of_Item_Used": 7}
#     ]

#     db = PostgresqlDatabase("db", host="localhost", user="postgres", password="postgres")
    
#     # Insert the sample data into the database

#     with db.atomic():
#         Volunteer.insert_many(volunteers_sample_data).execute()
#         Service_Providers.insert_many(service_providers_sample_data).execute()
#         Services.insert_many(services_sample_data).execute()
#         Neighbor.insert_many(neighbors_sample_data).execute()
#         Visit_Record.insert_many(visit_records_sample_data).execute()
#         Visit_Service.insert_many(visit_services_sample_data).execute()    
#         Inventory.insert_many(inventory_sample_data).execute()
#         Inventory_Usage.insert_many(inventory_usage_sample_data).execute()  
 
