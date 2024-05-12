from datetime import datetime
from models import *
from peewee import *
db = PostgresqlDatabase("db", host="localhost", user="postgres", password="postgres")

def generate_sample_data():
    # Sample data for Service_Providers table
    def service_providers_sample_data():
        return [
            {
                'Organization_Name': 'Up Initative',
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
                'ServiceType': 'Clothing Closet',
                'OrganizationID': 1,
                'ServiceDescription': 'Clothing closet service'
            },
            {
                'ServiceType': 'Laundry Service',
                'OrganizationID': 1,
                'ServiceDescription': 'Laundry service'
            },
            {
                'ServiceType': 'Food Security',
                'OrganizationID': 1,
                'ServiceDescription': 'Food security service'
            },
            {
                'ServiceType': 'Case Management',
                'OrganizationID': 1,
                'ServiceDescription': 'Case management service'
            },
            {
                'ServiceType': 'Hygiene Kits',
                'OrganizationID': 1,
                'ServiceDescription': 'Hygiene kits distribution'
            },
            {
                'ServiceType': 'Public Transportation and Gas Assistance',
                'OrganizationID': 1,
                'ServiceDescription': 'Assistance with public transportation and gas expenses'
            },
            {
                'ServiceType': 'Cleaning',
                'OrganizationID': 4,
                'ServiceDescription': 'Weekly cleaning service'
            },
            {
                'ServiceType': 'Food Delivery',
                'OrganizationID': 2,
                'ServiceDescription': 'Monthly food delivery'
            },
            {
                'ServiceType': 'Clothing Donation',
                'OrganizationID': 3,
                'ServiceDescription': 'Clothing donation drive'
            },
            {
                'ServiceType': 'Medical Assistance',
                'OrganizationID': 5,
                'ServiceDescription': 'Medical check-up and consultation'
            },
            {
                'ServiceType': 'Job Training',
                'OrganizationID': 5,
                'ServiceDescription': 'Job training workshop'
            }
        ]


    # Sample data for Volunteer table
    def volunteers_sample_data():
        return [
            {
                'FirstName': 'Alyssa',
                'LastName': 'Smith',
                'Password': '123',
                'Email': 'alyssa@example.com',
                'Phone': '987-654-3210',
                'HasRecordAccess': True
            },
            {
                'FirstName': 'Bo',
                'LastName': 'Johnson',
                'Password': 'qwerty456',
                'Email': 'bo@example.com',
                'Phone': '111-222-3333',
                'HasRecordAccess': False
            },
            {
                'FirstName': 'Eve',
                'LastName': 'Davis',
                'Password': 'pass1234',
                'Email': 'eve@example.com',
                'Phone': '444-555-6666',
                'HasRecordAccess': True
            },
            {
                'FirstName': 'Mike',
                'LastName': 'Wilson',
                'Password': 'abcd1234',
                'Email': 'mike@example.com',
                'Phone': '777-888-9999',
                'HasRecordAccess': False
            },
            {
                'FirstName': 'Jasmine',
                'LastName': 'Wilson',
                'Password': 'password789',
                'Email': 'Jasmine@example.com',
                'Phone': '555-666-7777',
                'HasRecordAccess': True
            }
        ]

# Sample data for Neighbor table
    def neighbors_sample_data():
        return [
            {
                'FirstName': 'Bob',
                'LastName': 'Johnson',
                'DateOfBirth': '1990-05-15',
                'Phone': '555-123-4567',
                'Location': '123 Main St',
                'Email': 'bob@example.com',
                'HasStateID': True,
                'HasPet': False,
                'HasChildren': False,
                'HasMedication': True,
                'HasFoodInsecurity': False,
                'HasTransportation': True,
                'HasJob': True,
                'HasHousing': True,
                'HasInsurance': True,
                'HasIncome': True,
                'Notes': 'Needs assistance with medication management'
            },
            {
                'FirstName': 'Emily',
                'LastName': 'Davis',
                'DateOfBirth': '1985-09-20',
                'Phone': '111-222-3333',
                'Location': '456 Elm St',
                'Email': 'emily@example.com',
                'HasStateID': False,
                'HasPet': True,
                'HasChildren': True,
                'HasMedication': False,
                'HasFoodInsecurity': True,
                'HasTransportation': False,
                'HasJob': False,
                'HasHousing': True,
                'HasInsurance': False,
                'HasIncome': False,
                'Notes': 'Requires food assistance and transportation support'
            },
            {
                'FirstName': 'Michael',
                'LastName': 'Wilson',
                'DateOfBirth': '1978-02-10',
                'Phone': '444-555-6666',
                'Location': '789 Oak Ave',
                'Email': 'michael@example.com',
                'HasStateID': True,
                'HasPet': False,
                'HasChildren': False,
                'HasMedication': False,
                'HasFoodInsecurity': False,
                'HasTransportation': True,
                'HasJob': True,
                'HasHousing': True,
                'HasInsurance': True,
                'HasIncome': True,
                'Notes': 'No specific assistance needed at the moment'
            },
            {
                'FirstName': 'Sarah',
                'LastName': 'Brown',
                'DateOfBirth': '1995-12-03',
                'Phone': '777-888-9999',
                'Location': '321 Pine Rd',
                'Email': 'sarah@example.com',
                'HasStateID': True,
                'HasPet': True,
                'HasChildren': True,
                'HasMedication': True,
                'HasFoodInsecurity': False,
                'HasTransportation': True,
                'HasJob': True,
                'HasHousing': True,
                'HasInsurance': True,
                'HasIncome': True,
                'Notes': 'Needs occasional help with childcare'
            },
            {
                'FirstName': 'David',
                'LastName': 'Taylor',
                'DateOfBirth': '1982-07-25',
                'Phone': '222-333-4444',
                'Location': '654 Cedar Ln',
                'Email': 'david@example.com',
                'HasStateID': False,
                'HasPet': False,
                'HasChildren': False,
                'HasMedication': False,
                'HasFoodInsecurity': False,
                'HasTransportation': True,
                'HasJob': False,
                'HasHousing': False,
                'HasInsurance': False,
                'HasIncome': False,
                'Notes': 'Seeking assistance with housing and employment'
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
                'Description_of_Item': 'Mop and bucket',
                'ExpirationDate': '2024-12-31',
                'Number_Of_Item': 10
            },
            {
                'NameOfItem': 'Food Items',
                'Description_of_Item': 'Canned goods',
                'ExpirationDate': '2023-09-30',
                'Number_Of_Item': 50
            },
            {
                'NameOfItem': 'Clothing',
                'Description_of_Item': 'T-shirts and jeans',
                'ExpirationDate': '2023-09-30', #TODO listed as cannot be NULL?
                'Number_Of_Item': 20
            },
            {
                'NameOfItem': 'Medical Supplies',
                'Description_of_Item': 'Bandages and antiseptic',
                'ExpirationDate': '2025-06-30',
                'Number_Of_Item': 15
            },
            {
                'NameOfItem': 'Stationery',
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

