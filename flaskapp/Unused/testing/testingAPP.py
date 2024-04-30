from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash #Using for passwords 
from flask_cors import CORS #to allow the front end to communicate with the back end
from models import *


app = Flask(__name__)

app.config.from_object(__name__)
CORS(app)

@app.route('/api/Add_Visit', methods=['GET'])
def add_visit():
    data_to_send = {
        "neighbors": {
            "Name1": "Alice Johnson",
            "Name2": "Bob Smith",
            "Name3": "Catherine Williams"
        },
        "volunteers": {
            "volName1": "John Doe",
            "volName2": "Jane Smith",
            "volName3": "Emily Jones"
        },
        "services": {
            "ServiceID1": "SP001",
            "ServiceID2": "SP002"
            
        },
        "inventory": {
            "Item1": "Canned Beans",
            "Item2": "Winter Coats"
            
        }
    }

    return jsonify(data_to_send)
# def add_visit():
#     neighbors_sample_data = [
#         {
#             "NeighborID": 1,
#             "VolunteerID": 1,
#             "OrganizationID": 8,
#             "FirstName": "Alice",
#             "LastName": "Johnson",
#             "DateOfBirth": datetime.date(1980, 5, 15).isoformat(),
#             "Phone": "555-0201",
#             "Location": "123 Elm Street, Springfield",
#             "Email": "alice.j@example.com",
#             "Created_date": datetime.datetime.now().isoformat(),
#             "HasStateID": True,
#             "HasPet": False
#         },
#         {
#             "NeighborID": 2,
#             "VolunteerID": 2,
#             "OrganizationID": 9,
#             "FirstName": "Bob",
#             "LastName": "Smith",
#             "DateOfBirth": datetime.date(1975, 8, 25).isoformat(),
#             "Phone": "555-0202",
#             "Location": "456 Maple Avenue, Springfield",
#             "Email": "bob.s@example.com",
#             "Created_date": datetime.datetime.now().isoformat(),
#             "HasStateID": False,
#             "HasPet": True
#         }
#     ]

#     volunteers_sample_data = [
#         {"FirstName": "John", "LastName": "Doe", "Password": "hashed_password1", "Email": "john.doe@example.com", "Phone": "555-0101", "HasRecordAccess": True},
#         {"FirstName": "Jane", "LastName": "Smith", "Password": "hashed_password2", "Email": "jane.smith@example.com", "Phone": "555-0102", "HasRecordAccess": False}
#     ]

#     services_sample_data = [
#         {"ServiceType": "Meal Delivery", "OrganizationID": "SP002"},
#         {"ServiceType": "Legal Aid", "OrganizationID": "SP001"}
#     ]

#     inventory_sample_data = [
#         {"InventoryID": 1, "NameOfItem": "Canned Beans", "VolunteerID": 1, "Description_of_Item": "Food item", "ExpirationDate": datetime.date(2025, 12, 31).isoformat(), "Number_Of_Item": 100, "Inventory_UseID": 1},
#         {"InventoryID": 2, "NameOfItem": "Winter Coats", "VolunteerID": 2, "Description_of_Item": "Clothing item", "ExpirationDate": datetime.date(2024, 11, 30).isoformat(), "Number_Of_Item": 40, "Inventory_UseID": 2}
#     ]

#     # Combine all data into a single dictionary
#     data_to_send = {
#         "neighbors": neighbors_sample_data,
#         "volunteers": volunteers_sample_data,
#         "services": services_sample_data,
#         "inventory": inventory_sample_data
#     }
#     return jsonify(data_to_send)

    # Send data to the Flask API
    # response = requests.get('http://localhost:5000/api/Add_Visit', json=json_data)
    # print(response.text)
    #     return jsonify({"status": "success", "data_received": data}), 200


if __name__ == '__main__':
    app.run(debug=True)
