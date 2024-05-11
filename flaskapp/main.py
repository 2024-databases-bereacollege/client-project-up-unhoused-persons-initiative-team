from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash #Using for passwords 
from flask_cors import CORS #to allow the front end to communicate with the back end
from models import *
from datetime import date, datetime
from playhouse.shortcuts import model_to_dict, dict_to_model

# This file runs the flask back end. It is the main file that runs the back end.

app = Flask(__name__)
app.secret_key = 'postgres'

app.config.from_object(__name__)
CORS(app)

db.connect()


# LOGIN PAGE ##########################################################
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    print('Received login data:', data)
    last_name = data.get('username')
    password = data.get('password')
    print(f"Received login request for username: {last_name}")

    # Check if the required fields are present
    if not last_name or not password:
        print('Username and password are required')
        return jsonify({'error': 'Username and password are required'}), 400

    # Query the volunteer with the provided last name
    volunteer = Volunteer.get_or_none(Volunteer.LastName == last_name)
    if volunteer:
        print(f"Found volunteer: {volunteer.to_dict()}")
        if check_password_hash(volunteer.Password, password):
            # Login successful
            session['logged_in'] = True
            volunteer_data = volunteer.to_dict()
            volunteer_data['has_record_access'] = volunteer.HasRecordAccess  # Include HasRecordAccess in the response
            print('Login successful')
            return jsonify({'message': 'Login successful', 'volunteer': volunteer_data}), 200
        else:
            print("Password does not match")
            return jsonify({'error': 'Invalid username or password'}), 401
    else:
        print("Volunteer not found")
        return jsonify({'error': 'Invalid username or password'}), 401
# ADD VISIT SECTION ##########################################
# Function to get neighbors list
def get_neighborsAV():
    neighbors_query = Neighbor.select(
        Neighbor.NeighborID,
        Neighbor.FirstName,
        Neighbor.LastName
    )

    neighbors_list = [
        {
            'NeighborID': neighbor.NeighborID,
            'FullName': f"{neighbor.FirstName} {neighbor.LastName}" #TODO update in case we dont have full name
        } for neighbor in neighbors_query
    ]
    return neighbors_list

# Function to get volunteers list
def get_volunteersAV():
    volunteers_query = Volunteer.select(
        Volunteer.VolunteerID, 
        Volunteer.FirstName, 
        Volunteer.LastName
    )
    return [{
        'VolunteerID': volunteer.VolunteerID,
        'FullName': f"{volunteer.FirstName} {volunteer.LastName}"
    } for volunteer in volunteers_query]

# Function to get services list
def get_servicesAV():
    services_query = Services.select()
    return [{
        'ServiceID': service.ServiceID,
        'ServiceType': service.ServiceType
    } for service in services_query]

# Function to get inventory list
def get_inventoryAV():
    inventory_query = Inventory.select()
    return [{
        'InventoryID': inventory.InventoryID,
        'NameOfItem': inventory.NameOfItem,
        'Number_Of_Item': inventory.Number_Of_Item
    } for inventory in inventory_query]

# API endpoint to get visit details
@app.route('/api/Add_Visit', methods=['GET'])
def get_visit(): 
    data = {
        'neighbors': get_neighborsAV(),
        'volunteers': get_volunteersAV(),
        'services': get_servicesAV(),
        'inventory': get_inventoryAV()
    }
    return jsonify(data)

# API endpoint to add a visit
@app.route('/api/visit_logs', methods=['POST'])
def create_visit_log():
    data = request.get_json()
    print('Received request data:', data)

    neighbor_id = data.get('NeighborID')
    volunteer_id = data.get('VolunteerID')
    service_id = data.get('ServiceID')
    description = data.get('Description')
    visit_date_str = data.get('Date')
    visit_date = datetime.strptime(visit_date_str, '%Y-%m-%d').date() # Convert visit_date_str to a date object

    # Create a new Visit_Service record
    visit_service = Visit_Service.create(
        ServiceID=service_id,
        Description=description,
        Date=visit_date
    )
    print('Created Visit_Service record:', visit_service)

    # Create a new Visit_Record record
    visit_record = Visit_Record.create(
        NeighborID=neighbor_id,
        VolunteerID=volunteer_id,
        RecordID=visit_service.RecordID
    )
    print('Created Visit_Record record:', visit_record)

    visit_log = {
        'VisitDate': visit_service.Date.isoformat(),
        'ServiceName': visit_service.ServiceID.ServiceType,
        'Description': visit_service.Description,
        'VolunteerName': f"{visit_record.VolunteerID.FirstName} {visit_record.VolunteerID.LastName}",
        'NeighborFirstName': visit_record.NeighborID.FirstName,
        'NeighborLastName': visit_record.NeighborID.LastName,
        'NeighborID': visit_record.NeighborID.NeighborID,
        #'ServiceProvider': visit_service.ServiceID.service_providers.Organization_Name
    }

    return jsonify(visit_log)

################ volunteers below ############################


# API endpoint to get all volunteers
@app.route('/api/volunteers', methods=['GET']) #GET request to get all volunteers
def get_volunteers():
    # Query all volunteers from the database
    query = Volunteer.select()
    volunteers = [volunteer.to_dict() for volunteer in query]  # Convert models to dictionaries
    
    return jsonify(volunteers)

# API endpoint to create a volunteer
@app.route('/api/volunteers', methods=['POST'])
def create_volunteer():
    data = request.get_json()
    # Remove the VolunteerID field from the data
    data.pop('VolunteerID', None)
    
    # Get the plain-text password from the request data
    password = data.pop('Password', None)
    
    if password:
        # Hash the password
        hashed_password = generate_password_hash(password)
        # Update the data dictionary with the hashed password
        data['Password'] = hashed_password
    
    volunteer = Volunteer(**data)
    volunteer.save()
    return jsonify(volunteer.to_dict()), 201

# API endpoint to update a volunteer
@app.route('/api/volunteers/<int:volunteer_id>', methods=['PUT']) #PUT request to update a volunteer
def update_volunteer(volunteer_id):
    data = request.get_json()
    # Remove the VolunteerID field from the data
    data.pop('VolunteerID', None)
    volunteer = Volunteer.get_or_none(Volunteer.VolunteerID == volunteer_id)
    if volunteer:
        for key, value in data.items():
            setattr(volunteer, key, value)
        volunteer.save()
        return jsonify(volunteer.to_dict())
    else:
        return jsonify({'error': 'Volunteer not found'}), 404

# API endpoint to delete a volunteer
@app.route('/api/volunteers/<int:volunteer_id>', methods=['DELETE']) #DELETE request to delete a volunteer
def delete_volunteer(volunteer_id):
    volunteer = Volunteer.get_by_id(volunteer_id)
    volunteer.delete_instance()
    return '', 204

################ volunteers above ############################

################ neighbors below ############################ 

# API endpoint to get all neighbors   
@app.route('/api/neighbors', methods=['GET'])
def get_neighbors():
    neighbors = [
        {
            'NeighborID': neighbor.NeighborID,
            'FirstName': neighbor.FirstName,
            'LastName': neighbor.LastName,
            'DateOfBirth': neighbor.DateOfBirth.strftime('%Y-%m-%d') if neighbor.DateOfBirth else None,
            'Phone': neighbor.Phone,
            'Location': neighbor.Location,
            'Email': neighbor.Email,
            'Created_date': neighbor.Created_date.strftime('%Y-%m-%d') if neighbor.Created_date else None,
            'HasStateID': neighbor.HasStateID,
            'HasPet': neighbor.HasPet,
            'HasChildren': neighbor.HasChildren,
            'HasMedication': neighbor.HasMedication,
            'HasFoodInsecurity': neighbor.HasFoodInsecurity,
            'HasTransportation': neighbor.HasTransportation,
            'HasJob': neighbor.HasJob,
            'HasHousing': neighbor.HasHousing,
            'HasInsurance': neighbor.HasInsurance,
            'HasIncome': neighbor.HasIncome,
            'Notes': neighbor.Notes
        }
        for neighbor in Neighbor.select()
    ]
    return jsonify(neighbors)

# API endpoint to create a neighbor
@app.route('/api/neighbors', methods=['POST'])
def create_neighbor():
    data = request.get_json()

    # Handle DateOfBirth field
    date_of_birth = data.get('DateOfBirth')
    if date_of_birth:
        try:
            date_of_birth_value = date.fromisoformat(date_of_birth)
        except ValueError:
            # Handle invalid date format
            return jsonify({'error': 'Invalid date format for DateOfBirth'}), 400
    else:
        date_of_birth_value = None

    # Create a new Neighbor instance
    neighbor_data = {
        'FirstName': data.get('FirstName'),
        'LastName': data.get('LastName'),
        'DateOfBirth': date_of_birth_value,
        'Phone': data.get('Phone'),
        'Location': data.get('Location'),
        'Email': data.get('Email'),
        'Created_date': datetime.now(),
        'HasStateID': data.get('HasStateID', False),
        'HasPet': data.get('HasPet', False),
        'HasChildren': data.get('HasChildren', False),
        'HasMedication': data.get('HasMedication', False),
        'HasFoodInsecurity': data.get('HasFoodInsecurity', False),
        'HasTransportation': data.get('HasTransportation', False),
        'HasJob': data.get('HasJob', False),
        'HasHousing': data.get('HasHousing', False),
        'HasInsurance': data.get('HasInsurance', False),
        'HasIncome': data.get('HasIncome', False),
        'Notes': data.get('Notes')
    }

    neighbor = Neighbor(**neighbor_data)
    neighbor.save()

    return jsonify(neighbor.to_dict()), 201

# API endpoint to edit a neighbor
@app.route('/api/neighbors/<int:neighbor_id>', methods=['PUT'])
def update_neighbor(neighbor_id):
    data = request.get_json()
    neighbor = Neighbor.get_or_none(Neighbor.NeighborID == neighbor_id)
    if neighbor:
        for key, value in data.items():
            if key == 'DateOfBirth':
                if value:
                    try:
                        date_value = date.fromisoformat(value)
                    except ValueError:
                        return jsonify({'error': 'Invalid date format for DateOfBirth'}), 400
                else:
                    date_value = None
                setattr(neighbor, key, date_value)
            else:
                setattr(neighbor, key, value)
        neighbor.save()
        return jsonify(neighbor.to_dict())
    else:
        return jsonify({'error': 'Neighbor not found'}), 404
# API endpoint to delete a neighbor
@app.route('/api/neighbors/<int:neighbor_id>', methods=['DELETE'])
def delete_neighbor(neighbor_id):
    neighbor = Neighbor.get_or_none(Neighbor.NeighborID == neighbor_id)
    if neighbor:
        neighbor.delete_instance()
        return '', 204
    else:
        return jsonify({'error': 'Neighbor not found'}), 404

################ neighbors above ############################

################ Services only below ##################
# API endpoint to get services
@app.route('/api/services', methods=['GET'])
def get_services_alone():
    query = Services.select()
    services = [service.to_dict() for service in query]
    return jsonify(services)

################ Services only above ##################
    

################ ServicesAndProviders Table below ############################

# API endpoint to get services for join table
@app.route('/api/ServicesAndProviders', methods=['GET'])
def get_services():
    query = (
        Services
        .select(Services, fn.COUNT(Visit_Record.NeighborID.distinct()).alias('TotalNeighbors'))
        .join(Service_Providers, on=(Services.OrganizationID == Service_Providers.OrganizationID))
        .switch(Services)
        .join(Visit_Service, JOIN.LEFT_OUTER)
        .join(Visit_Record, JOIN.LEFT_OUTER)
        .group_by(Services)
    )
    
    services = []
    for service in query:
        service_dict = model_to_dict(service)
        service_dict['Organization_Name'] = service.OrganizationID.Organization_Name
        service_dict['ContactPerson'] = service.OrganizationID.ContactPerson
        service_dict['Email'] = service.OrganizationID.Email
        service_dict['Phone'] = service.OrganizationID.Phone
        service_dict['DateOfStart'] = service.OrganizationID.DateOfStart
        service_dict['TotalNeighbors'] = service.TotalNeighbors
        service_dict['ServiceDescription'] = service.ServiceDescription
        service_dict['OrganizationID']
        
        services.append(service_dict)
    
    return jsonify(services)

# API endpoint to get service providers - This is to display them in the buttons!
@app.route('/api/service_providers', methods=['GET'])
def get_service_providers():
    query = Service_Providers.select()
    service_providers = [provider.to_dict() for provider in query]
    return jsonify(service_providers)

# API endpoint to create services on ServicesAndProviders page
@app.route('/api/services', methods=['POST'])
def create_service_on_ServicesAndProvidersPage():
    data = request.get_json()
    print('Received request data:', data)

    service_type = data.get('ServiceType')
    organization_id = data.get('OrganizationID')
    service_description = data.get('ServiceDescription')

    # Create a new Services record
    service = Services.create(
        ServiceType=service_type,
        OrganizationID=organization_id,
        ServiceDescription=service_description
    )
    print('Created Services record:', service)

    service_data = {
        'ServiceID': service.ServiceID,
        'ServiceType': service.ServiceType,
        'ServiceDescription': service.ServiceDescription,
        'OrganizationName': service.OrganizationID.Organization_Name
    }

    return jsonify(service_data), 201

# API endpoint to create service providers on ServicesAndProviders page
@app.route('/api/service_providers', methods=['POST'])
def create_service_provider():
    data = request.get_json()
    print('Received request data:', data)

    organization_name = data.get('Organization_Name')
    contact_person = data.get('ContactPerson')
    email = data.get('Email')
    phone = data.get('Phone')
    date_of_start_str = data.get('DateOfStart')
    date_of_start = datetime.strptime(date_of_start_str, '%Y-%m-%d').date()

    # Create a new Service_Providers record
    service_provider = Service_Providers.create(
        Organization_Name=organization_name,
        ContactPerson=contact_person,
        Email=email,
        Phone=phone,
        DateOfStart=date_of_start
    )
    print('Created Service_Providers record:', service_provider)

    service_provider_data = {
        'OrganizationID': service_provider.OrganizationID,
        'Organization_Name': service_provider.Organization_Name,
        'ContactPerson': service_provider.ContactPerson,
        'Email': service_provider.Email,
        'Phone': service_provider.Phone,
        'DateOfStart': service_provider.DateOfStart.isoformat()
    }

    return jsonify(service_provider_data), 201

# API endpoint to edit services on ServicesAndProviders page
@app.route('/api/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    data = request.get_json()
    print('Received request data:', data)

    service_type = data.get('ServiceType')
    organization_id = data.get('OrganizationID')
    service_description = data.get('ServiceDescription')

    try:
        service = Services.get(Services.ServiceID == service_id)
        service.ServiceType = service_type
        service.OrganizationID = organization_id
        service.ServiceDescription = service_description
        service.save()

        updated_service_data = {
            'ServiceID': service.ServiceID,
            'ServiceType': service.ServiceType,
            'ServiceDescription': service.ServiceDescription,
            'OrganizationName': service.OrganizationID.Organization_Name
        }

        return jsonify(updated_service_data), 200
    except Services.DoesNotExist:
        return jsonify({'error': 'Service not found'}), 404

# API endpoint to edit service providers on ServicesAndProviders page
@app.route('/api/service_providers/<int:organization_id>', methods=['PUT'])
def update_service_provider(organization_id):
    data = request.get_json()
    print('Received request data:', data)

    organization_name = data.get('Organization_Name')
    contact_person = data.get('ContactPerson')
    email = data.get('Email')
    phone = data.get('Phone')
    date_of_start_str = data.get('DateOfStart')
    if date_of_start_str:
        date_of_start = datetime.strptime(date_of_start_str, '%Y-%m-%d').date()
    else:
        date_of_start = datetime(2024, 1, 1).date()  

    try:
        service_provider = Service_Providers.get(Service_Providers.OrganizationID == organization_id)
        service_provider.Organization_Name = organization_name
        service_provider.ContactPerson = contact_person
        service_provider.Email = email
        service_provider.Phone = phone
        service_provider.DateOfStart = date_of_start
        service_provider.save()

        updated_service_provider_data = {
            'OrganizationID': service_provider.OrganizationID,
            'Organization_Name': service_provider.Organization_Name,
            'ContactPerson': service_provider.ContactPerson,
            'Email': service_provider.Email,
            'Phone': service_provider.Phone,
            'DateOfStart': service_provider.DateOfStart.isoformat()
        }

        return jsonify(updated_service_provider_data), 200
    except Service_Providers.DoesNotExist:
        return jsonify({'error': 'Service provider not found'}), 404

    
    # API endpoint to delete a service from join table
@app.route('/api/ServicesAndProviders/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    try:
        service = Services.get(Services.ServiceID == service_id)
        service.delete_instance()
        return jsonify({'message': 'Service deleted successfully'})
    except Services.DoesNotExist:
        return jsonify({'error': 'Service not found'}), 404



################ ServicesAndProviders Table above  ############################


################ Visit Logs Below ##################################
    
# API endpoint to get visit logs
@app.route('/api/visit_logs', methods=['GET'])
def get_visit_logs():
    query = (Visit_Service
             .select(
                 Visit_Service.Date.alias('VisitDate'),
                 Services.ServiceType.alias('ServiceName'),
                 Visit_Service.Description,
                 Volunteer.FirstName.concat(' ').concat(Volunteer.LastName).alias('VolunteerName'),
                 Neighbor.FirstName.alias('NeighborFirstName'),
                 Neighbor.LastName.alias('NeighborLastName'),
                 Neighbor.NeighborID.alias('NeighborID'),
                 Service_Providers.Organization_Name.alias('ServiceProvider')

             )
             .join(Services)  # This joins Visit_Service to Services on the implicit foreign key relationship
             .join(Service_Providers)  # This joins Services to Service_Providers
             .switch(Visit_Service)  # Return to Visit_Service to join another table
             .join(Visit_Record)  # This joins Visit_Service to Visit_Record
             .join(Volunteer)  # This joins Visit_Record to Volunteer
             .join(Neighbor, on=(Visit_Record.NeighborID == Neighbor.NeighborID))  # This joins Visit_Record to Neighbor with an explicit join condition
             .order_by(Visit_Service.Date.desc()))

    result = [item for item in query.dicts()]
    return jsonify(result)


################ visit Logs above ############################

############### Individual Visit logs and neighbor profiles below ###################

# This query gets the neighbor details for the neighbor profile page
@app.route('/api/neighbors/<int:neighbor_id>', methods=['GET'])
def get_neighbor_details(neighbor_id):
    try:
        neighbor = Neighbor.get_by_id(neighbor_id)
        neighbor_info = {
            'NeighborID': neighbor.NeighborID,
            'FullName': f"{neighbor.FirstName} {neighbor.LastName}",
            'DateOfBirth': neighbor.DateOfBirth.strftime('%Y-%m-%d') if neighbor.DateOfBirth else None
        }
        return jsonify(neighbor_info), 200
    except Neighbor.DoesNotExist:
        return jsonify({'error': 'Neighbor not found'}), 404

#This query gets the visit records for the neighbor profile page
@app.route('/api/IndividualVisitLog', methods=['GET'])
def get_IndividualVisitLog():
    query = (Visit_Service
             .select(
                 Visit_Service.Date.alias('VisitDate'),
                 Services.ServiceType.alias('ServiceName'),
                 Visit_Service.Description,
                 Volunteer.FirstName.concat(' ').concat(Volunteer.LastName).alias('VolunteerName'),
                 Service_Providers.Organization_Name.alias('ServiceProvider')

             )
             .join(Services)  # This joins Visit_Service to Services on the implicit foreign key relationship
             .join(Service_Providers)  # This joins Services to Service_Providers
             .switch(Visit_Service)  # Return to Visit_Service to join another table
             .join(Visit_Record)  # This joins Visit_Service to Visit_Record
             .join(Volunteer)  # This joins Visit_Record to Volunteer
             .order_by(Visit_Service.Date.desc()))
    result = [item for item in query.dicts()]
    return jsonify(result)  

############### Individual Visit logs and neighbor profiles above ###################

#####################################################################################
#TODO everything underneath this line can be added, but is currently not in use. 
################ visit services below ############################
# API endpoint to get visit services
@app.route('/api/visit_services', methods=['GET'])
def get_visit_services():
    query = Visit_Service.select()
    visit_services = [service.to_dict() for service in query]
    return jsonify(visit_services)

# API endpoint to create visit services
@app.route('/api/visit_services', methods=['POST'])
def create_visit_service():
    data = request.get_json()
    visit_service = Visit_Service(**data)
    visit_service.save()
    return jsonify(visit_service.to_dict()), 201

# API endpoint to edit visit services
@app.route('/api/visit_services/<int:service_id>', methods=['PUT'])
def update_visit_service(service_id):
    data = request.get_json()
    visit_service = Visit_Service.get_or_none(Visit_Service.ServiceID == service_id)
    if visit_service:
        for key, value in data.items():
            setattr(visit_service, key, value)
        visit_service.save()
        return jsonify(visit_service.to_dict())
    else:
        return jsonify({'error': 'Visit Service not found'}), 404
    
# API endpoint to delete visit services
@app.route('/api/visit_services/<int:service_id>', methods=['DELETE'])
def delete_visit_service(service_id):
    visit_service = Visit_Service.get_or_none(Visit_Service.ServiceID == service_id)
    if visit_service:
        visit_service.delete_instance()
        return '', 204
    else:
        return jsonify({'error': 'Visit Service not found'}), 404
    
################ visit services above ############################
    
################ visit records below ############################
# API endpoint to get visit records
@app.route('/api/visit_records', methods=['GET'])
def get_visit_records():
    query = Visit_Record.select()
    visit_records = [record.to_dict() for record in query]
    return jsonify(visit_records)

# API endpoint to create visit records
@app.route('/api/visit_records', methods=['POST'])
def create_visit_record():
    data = request.get_json()
    visit_record = Visit_Record(**data)
    visit_record.save()
    return jsonify(visit_record.to_dict()), 201

# API endpoint to edit visit records
@app.route('/api/visit_records/<int:record_id>', methods=['PUT'])
def update_visit_record(record_id):
    data = request.get_json()
    visit_record = Visit_Record.get_or_none(Visit_Record.RecordID == record_id)
    if visit_record:
        for key, value in data.items():
            setattr(visit_record, key, value)
        visit_record.save()
        return jsonify(visit_record.to_dict())
    else:
        return jsonify({'error': 'Visit Record not found'}), 404
    
# API endpoint to delete visit records
@app.route('/api/visit_records/<int:record_id>', methods=['DELETE'])
def delete_visit_record(record_id):
    visit_record = Visit_Record.get_or_none(Visit_Record.RecordID == record_id)
    if visit_record:
        visit_record.delete_instance()
        return '', 204
    else:
        return jsonify({'error': 'Visit Record not found'}), 404
    
################ visit records above ############################
    
################ inventory below ############################
# API endpoint to get inverntory
@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    query = Inventory.select()
    inventory = [item.to_dict() for item in query]
    return jsonify(inventory)

# API endpoint to create inverntory
@app.route('/api/inventory', methods=['POST'])
def create_inventory():
    data = request.get_json()
    inventory = Inventory(**data)
    inventory.save()
    return jsonify(inventory.to_dict()), 201

# API endpoint to edit inverntory
@app.route('/api/inventory/<int:inventory_id>', methods=['PUT'])
def update_inventory(inventory_id):
    data = request.get_json()
    inventory = Inventory.get_or_none(Inventory.InventoryID == inventory_id)
    if inventory:
        for key, value in data.items():
            setattr(inventory, key, value)
        inventory.save()
        return jsonify(inventory.to_dict())
    else:
        return jsonify({'error': 'Inventory Item not found'}), 404
    
# API endpoint to delete inverntory
@app.route('/api/inventory/<int:inventory_id>', methods=['DELETE'])
def delete_inventory(inventory_id):
    inventory = Inventory.get_or_none(Inventory.InventoryID == inventory_id)
    if inventory:
        inventory.delete_instance()
        return '', 204
    else:
        return jsonify({'error': 'Inventory Item not found'}), 404
    
################ inventory above ############################
 
################ inventory usage below ############################



@app.route('/api/inventory_usageAD', methods=['GET'])
def get_inventory_usageAD():
    query = (Inventory
             .select(Inventory, Inventory_Usage, Visit_Record.Date.alias('VisitDate'))
             .join(Inventory_Usage, on=(Inventory.InventoryID == Inventory_Usage.Inventory_UseID))
             .join(Visit_Record, on=(Inventory_Usage.RecordID == Visit_Record.RecordID)))

    inventory_usage_data = []
    for inventory_item in query:
        item_dict = inventory_item.to_dict()
        item_dict['VisitDate'] = inventory_item.VisitDate.strftime('%Y-%m-%d')
        inventory_usage_data.append(item_dict)

    return jsonify(inventory_usage_data)

# API endpoint to get inverntory_usage
@app.route('/api/inventory_usage', methods=['GET'])
def get_inventory_usage():
    query = Inventory_Usage.select()
    inventory_usage = [usage.to_dict() for usage in query]
    return jsonify(inventory_usage)

# API endpoint to create inverntory_usage
@app.route('/api/inventory_usage', methods=['POST'])
def create_inventory_usage():
    data = request.get_json()
    inventory_usage = Inventory_Usage(**data)
    inventory_usage.save()
    return jsonify(inventory_usage.to_dict()), 201

# API endpoint to edit inverntory_usage
@app.route('/api/inventory_usage/<int:usage_id>', methods=['PUT'])
def update_inventory_usage(usage_id):
    data = request.get_json()
    inventory_usage = Inventory_Usage.get_or_none(Inventory_Usage.Inventory_UseID == usage_id)
    if inventory_usage:
        for key, value in data.items():
            setattr(inventory_usage, key, value)
        inventory_usage.save()
        return jsonify(inventory_usage.to_dict())
    else:
        return jsonify({'error': 'Inventory Usage not found'}), 404
    
# API endpoint to delete inverntory_usage
@app.route('/api/inventory_usage/<int:usage_id>', methods=['DELETE'])
def delete_inventory_usage(usage_id):
    inventory_usage = Inventory_Usage.get_or_none(Inventory_Usage.Inventory_UseID == usage_id)
    if inventory_usage:
        inventory_usage.delete_instance()
        return '', 204
    else:
        return jsonify({'error': 'Inventory Usage not found'}), 404
    
################ inventory usage above ############################




if __name__ == '__main__':
    app.run(debug=True)

