from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash #Using for passwords 
from flask_cors import CORS #to allow the front end to communicate with the back end
from models import *
from datetime import date, datetime
from playhouse.shortcuts import model_to_dict, dict_to_model


app = Flask(__name__)
app.secret_key = 'postgres'

app.config.from_object(__name__)
CORS(app)

db.connect()
#db.create_tables([Volunteer], safe=True)


# LOGIN PAGE ##########################################################
@app.route('/api/login', methods=['POST'])
def login():

    data = request.get_json()
    last_name = data.get('username')
    password = data.get('password')

    print(f"Received login request for username: {last_name}")  # Add logging statement

    # Check if the required fields are present
    if not last_name or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Query the volunteer with the provided last name
    volunteer = Volunteer.get_or_none(Volunteer.LastName == last_name)

    if volunteer:
        print(f"Found volunteer: {volunteer.to_dict()}")  # Add logging statement
        if check_password_hash(volunteer.Password, password):
            # Login successful
            session['logged_in'] = True
            volunteer_data = volunteer.to_dict()
            return jsonify({'message': 'Login successful', 'volunteer': volunteer_data}), 200
        else:
            print("Password does not match")  # Add logging statement
    else:
        print("Volunteer not found")  # Add logging statement

    # Invalid username or password
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
    

################ services below - Along with editing service providers ############################

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

# API endpoint to edit a service
@app.route('/api/ServicesAndProviders/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    data = request.get_json()
    print(f"Received data for updating service: {data}")  # Add logging statement
    try:
        service = Services.get(Services.ServiceID == service_id)
        service.ServiceType = data.get('ServiceType', service.ServiceType)
        service.ServiceDescription = data.get('ServiceDescription', service.ServiceDescription)
        service.OrganizationID = data.get('OrganizationID', service.OrganizationID)
        service.save()
        print(f"Service updated successfully: {service.to_dict()}")  # Add logging statement
        return jsonify({'message': 'Service updated successfully'})
    except Services.DoesNotExist:
        return jsonify({'error': 'Service not found'}), 404

# API endpoint to edit a service provider
@app.route('/api/ServicesAndProviders/<int:organization_id>', methods=['PUT'])
def update_service_provider(organization_id):
    data = request.get_json()
    print(f"Received data for updating service provider: {data}")  # Add logging statement
    try:
        provider = Service_Providers.get(Service_Providers.OrganizationID == organization_id)
        provider.Organization_Name = data.get('Organization_Name', provider.Organization_Name)
        provider.ContactPerson = data.get('ContactPerson', provider.ContactPerson)
        provider.Email = data.get('Email', provider.Email)
        provider.Phone = data.get('Phone', provider.Phone)
        provider.DateOfStart = data.get('DateOfStart', provider.DateOfStart)
        provider.save()
        print(f"Service provider updated successfully: {provider.to_dict()}")  # Add logging statement
        return jsonify({'message': 'Service Provider updated successfully'})
    except Service_Providers.DoesNotExist:
        return jsonify({'error': 'Service Provider not found'}), 404


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







# # API endpoint to edit a service and its associated service provider
# @app.route('/api/ServicesAndProviders/<int:service_id>', methods=['PUT'])
# def update_service_and_provider(service_id):
#     data = request.get_json()
    
#     try:
#         service = Services.get(Services.ServiceID == service_id)
#         provider = Service_Providers.get(Service_Providers.OrganizationID == service.OrganizationID)
        
#         # Update service fields
#         service.ServiceType = data.get('ServiceType', service.ServiceType)
#         service.ServiceDescription = data.get('ServiceDescription', service.ServiceDescription)
#         service.save()
        
#         # Update service provider fields
#         provider.Organization_Name = data.get('Organization_Name', provider.Organization_Name)
#         provider.ContactPerson = data.get('ContactPerson', provider.ContactPerson)
#         provider.Email = data.get('Email', provider.Email)
#         provider.Phone = data.get('Phone', provider.Phone)
#         provider.DateOfStart = data.get('DateOfStart', provider.DateOfStart)
#         provider.save()
        
#         return jsonify({'message': 'Service and provider updated successfully'})
#     except Services.DoesNotExist:
#         return jsonify({'error': 'Service not found'}), 404
#     except Service_Providers.DoesNotExist:
#         return jsonify({'error': 'Service Provider not found'}), 404



# # API endpoint to edit a service provider
# @app.route('/api/service_providers/<int:provider_id>', methods=['PUT'])
# def update_service_provider(provider_id):
#     data = request.get_json()
#     provider = Service_Providers.get_or_none(Service_Providers.OrganizationID == provider_id)
#     if provider:
#         for key, value in data.items():
#             setattr(provider, key, value)
#         provider.save()
#         return jsonify(provider.to_dict())
#     else:
#         return jsonify({'error': 'Service Provider not found'}), 404
    
    # API endpoint to delete a service from join table
@app.route('/api/ServicesAndProviders/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    try:
        service = Services.get(Services.ServiceID == service_id)
        service.delete_instance()
        return jsonify({'message': 'Service deleted successfully'})
    except Services.DoesNotExist:
        return jsonify({'error': 'Service not found'}), 404



################ services above - And service providers ############################


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
#TODO
#TODO
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


# Rest of the queries- These are all currently unused. 



# # 4. Count the number of times each service has been provided
# @app.route('/api/services/count', methods=['GET'])
# def get_service_counts():
#     query = (Visit_Service
#              .select(Visit_Service.ServiceID, fn.Count(Visit_Service.ServiceOrder).alias('Count'))
#              .group_by(Visit_Service.ServiceID))
#     service_counts = [{
#         'ServiceID': service.ServiceID,
#         'Count': service.Count
#     } for service in query]
#     return jsonify(service_counts)

# # 5. Get a list of items in the inventory that will expire within a specified period
# @app.route('/api/inventory/expiring', methods=['GET'])
# def get_expiring_inventory():
#     start_date = request.args.get('start_date')
#     end_date = request.args.get('end_date')
#     query = Inventory.select().where((Inventory.ExpirationDate >= start_date) & (Inventory.ExpirationDate <= end_date))
#     expiring_inventory = [item.to_dict() for item in query]
#     return jsonify(expiring_inventory)


# # 7. Find all visit records conducted on a specific date
# @app.route('/api/visit_records/date/<date:date_string>', methods=['GET'])
# def get_visit_records_on_date(date_string):
#     target_date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
#     query = Visit_Record.select().where(Visit_Record.Date == target_date)
#     visit_records = [record.to_dict() for record in query]
#     return jsonify(visit_records)

# # 8.Get list of services provided by a specific organization every year
# @app.route('/api/services/provider/<string:provider_id>/year/<int:year>', methods=['GET'])
# def get_services_by_provider_year(provider_id, year):
#     query = (Services
#              .select(Services, fn.COUNT(Visit_Record.RecordID).alias('ServiceCount'))
#              .join(Visit_Service)
#              .join(Visit_Record)
#              .where((Services.OrganizationID == provider_id) & (fn.EXTRACT('year', Visit_Record.Date) == year))
#              .group_by(Services))
#     services_by_year = [{
#         'ServiceID': service.ServiceID,
#         'ServiceType': service.ServiceType,
#         'ServiceCount': service.ServiceCount
#     } for service in query]
#     return jsonify(services_by_year)

# # 9. Get list of organization providing service with the list of service they each provide
# @app.route('/api/providers/services', methods=['GET'])
# def get_providers_with_services():
#     query = Service_Providers.select()
#     providers_with_services = []
#     for provider in query:
#         provider_data = provider.to_dict()
#         provider_data['Services'] = [service.ServiceType for service in provider.services]
#         providers_with_services.append(provider_data)
#     return jsonify(providers_with_services)

# #10 Get all visit records for a specific neighbor 
# @app.route('/api/visit_records/<int:neighbor_id>', methods=['GET'])
# def get_visit_records_for_neighbor(neighbor_id):
#     query = Visit_Record.select().where(Visit_Record.NeighborID == neighbor_id)
#     visit_records = [record.to_dict() for record in query]
#     return jsonify(visit_records)


# # 16. Get all visits conducted by a specific volunteer
# @app.route('/api/volunteers/<int:volunteer_id>/visits', methods=['GET'])
# def get_visits_by_volunteer(volunteer_id):
#     query = (Visit_Record
#              .select()
#              .join(Volunteer)
#              .where(Volunteer.VolunteerID == volunteer_id))
#     visits = [visit.to_dict() for visit in query]
#     return jsonify(visits)



# #10 Get all visit records for a specific neighbor
# @app.route('/api/visit_records/<int:neighbor_id>', methods=['GET'])
# def get_visit_records_for_neighbor(neighbor_id):
#     query = Visit_Record.select().where(Visit_Record.NeighborID == neighbor_id)
#     visit_records = [record.to_dict() for record in query]
#     return jsonify(visit_records)
# #11 Get neighbor details along with their visit records, services, and volunteers associated with those visit records.
# @app.route('/api/neighbor/<int:neighbor_id>', methods=['GET'])
# def get_neighbor_details(neighbor_id):
#     try:
#         neighbor = Neighbor.get_by_id(neighbor_id)
#         neighbor_info = {
#             'NeighborID': neighbor.NeighborID,
#             'FullName': f"{neighbor.FirstName} {neighbor.LastName}",
#             'DateOfBirth': neighbor.DateOfBirth.strftime('%Y-%m-%d')  # Format date of birth
#         }
#         visit_records_query = Visit_Record.select().where(Visit_Record.NeighborID == neighbor_id)
#         visit_records = []
#         for record in visit_records_query:
#             visit_info = {
#                 'VisitID': record.VisitID,
#                 'Date': record.Date.strftime('%Y-%m-%d'),  # Format visit date
#             }
#             services_query = Visit_Service.select().where(Visit_Service.RecordID == record.RecordID)
#             services_info = [service.ServiceType for service in services_query]
#             visit_info['Services'] = services_info
#             volunteers_query = Volunteer.select().join(Visit_Record).where(Visit_Record.RecordID == record.RecordID)
#             volunteers_info = [{
#                 'VolunteerID': volunteer.VolunteerID,
#                 'FullName': f"{volunteer.FirstName} {volunteer.LastName}"
#             } for volunteer in volunteers_query]
#             visit_info['Volunteers'] = volunteers_info
#             visit_records.append(visit_info)
#         return jsonify({
#             'NeighborInfo': neighbor_info,
#             'VisitRecords': visit_records
#         }), 200
#     except Neighbor.DoesNotExist:
#         return jsonify({'error': 'Neighbor not found'}), 404
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
# # 12. Get all visits conducted within a specified date range
# @app.route('/api/visit_records/range', methods=['GET'])
# def get_visits_in_date_range():
#     start_date = request.args.get('start_date')
#     end_date = request.args.get('end_date')
#     query = Visit_Record.select().where((Visit_Record.Date >= start_date) & (Visit_Record.Date <= end_date))
#     visits = [visit.to_dict() for visit in query]
#     return jsonify(visits)
# # 13. Get all neighbors who have not received any visits
# @app.route('/api/neighbors/no_visits', methods=['GET'])
# def get_neighbors_without_visits():
#     query = Neighbor.select().where(~(Neighbor.neighbor_records.exists()))
#     neighbors = [neighbor.to_dict() for neighbor in query]
#     return jsonify(neighbors)
# # 14. Get list of organization providing service with the list of service they each provide
# @app.route('/api/providers/services', methods=['GET'])
# def get_providers_with_services():
#     query = Service_Providers.select()
#     providers_with_services = []
#     for provider in query:
#         provider_data = provider.to_dict()
#         provider_data['Services'] = [service.ServiceType for service in provider.services]
#         providers_with_services.append(provider_data)
#     return jsonify(providers_with_services)
# # 15.Get all volunteers who have provided a specific service
# @app.route('/api/services/<int:service_id>/volunteers', methods=['GET'])
# def get_volunteers_for_service(service_id):
#     query = (Volunteer
#              .select(Volunteer)
#              .join(Visit_Record)
#              .join(Visit_Service)
#              .where(Visit_Service.ServiceID == service_id))
#     volunteers = [volunteer.to_dict() for volunteer in query]
#     return jsonify(volunteers)
# # 16. Get all visits conducted by a specific volunteer
# @app.route('/api/volunteers/<int:volunteer_id>/visits', methods=['GET'])
# def get_visits_by_volunteer(volunteer_id):
#     query = (Visit_Record
#              .select()
#              .join(Volunteer)
#              .where(Volunteer.VolunteerID == volunteer_id))
#     visits = [visit.to_dict() for visit in query]
#     return jsonify(visits)


    # # Update Volunteer
    # volunteer_id = volunteer_data.get('volunteer_id')
    # volunteer = Volunteer.get_or_none(Volunteer.VolunteerID == volunteer_id)
    # if volunteer:
    #     for key, value in volunteer_data.items():
    #         if key != 'volunteer_id':  # Exclude the ID from the fields to update
    #             setattr(volunteer, key, value)
    #     volunteer.save()
    #     response['volunteer'] = volunteer.to_dict()
    # else:
    #     return jsonify({'error': 'Volunteer not found'}), 404

    # return jsonify(response)


# # API endpoint to edit visit_log after adding a visit
# @app.route('/api/IndividualVisitLog', methods=['PUT'])
# def update_visit_log():
#     data = request.get_json()
#     inventory_data = data.get('inventory')
#     visit_service_data = data.get('visit_service')
#     volunteer_data = data.get('volunteer')

#     response = {}
#     # Update Inventory
#     inventory_id = inventory_data.get('inventory_id')
#     inventory = Inventory.get_or_none(Inventory.InventoryID == inventory_id)
#     if inventory:
#         for key, value in inventory_data.items():
#             if key != 'inventory_id':  # Exclude the ID from the fields to update
#                 setattr(inventory, key, value)
#         inventory.save()
#         response['inventory'] = inventory.to_dict()
#     else:
#         return jsonify({'error': 'Inventory not found'}), 404

#     # Update Visit Service
#     record_id = visit_service_data.get('record_id')
#     visit_service = Visit_Service.get_or_none(Visit_Service.RecordID == record_id)
#     if visit_service:
#         for key, value in visit_service_data.items():
#             if key != 'record_id':  # Exclude the ID from the fields to update
#                 setattr(visit_service, key, value)
#         visit_service.save()
#         response['visit_service'] = visit_service.to_dict()
#     else:
#         return jsonify({'error': 'Visit service record not found'}), 404

##############################################################

# @app.route('/api/services', methods=['GET'])
# def get_services():
#     query = (Services
#              .select(Services, fn.COUNT(fn.DISTINCT(Visit_Record.NeighborID)).alias('TotalNeighbors'))
#              .join(Visit_Service)
#              .join(Visit_Record)
#              .group_by(Services))

#     services = []
#     for service in query:
#         service_dict = service.to_dict()
#         # Add the TotalNeighbors count to the dictionary that is being sent to frontend
#         service_dict['TotalNeighbors'] = service.TotalNeighbors
#         services.append(service_dict)

#     return jsonify(services)

# API endpoint to create services
# @app.route('/api/services', methods=['POST'])
# def create_service():
#     data = request.get_json()
#     service = Services(**data)
#     service.save()
#     return jsonify(service.to_dict()), 201

# # API endpoint to edit services
# @app.route('/api/services/<int:service_id>', methods=['PUT'])
# def update_service(service_id):
#     data = request.get_json()
#     service = Services.get_or_none(Services.ServiceID == service_id)
#     if service:
#         for key, value in data.items():
#             setattr(service, key, value)
#         service.save()
#         return jsonify(service.to_dict())
#     else:
#         return jsonify({'error': 'Service not found'}), 404

# API endpoint to delete services
# @app.route('/api/services/<int:service_id>', methods=['DELETE'])
# def delete_service(service_id):
#     service = Services.get_or_none(Services.ServiceID == service_id)
#     if service:
#         service.delete_instance()
#         return '', 204
#     else:
#         return jsonify({'error': 'Service not found'}), 404
    
################ service providers below ############################

# # API endpoint to get service providers
# @app.route('/api/service_providers', methods=['GET'])
# def get_service_providers():
#     query = Service_Providers.select()
#     service_providers = [provider.to_dict() for provider in query]
#     return jsonify(service_providers)

# # API endpoint to create service providers
# @app.route('/api/service_providers', methods=['POST'])
# def create_service_provider():
#     data = request.get_json()
#     provider = Service_Providers(**data)
#     provider.save()
#     return jsonify(provider.to_dict()), 201

# # API endpoint to edit service providers
# @app.route('/api/service_providers/<int:provider_id>', methods=['PUT'])
# def update_service_provider(provider_id):
#     data = request.get_json()
#     provider = Service_Providers.get_or_none(Service_Providers.OrganizationID == provider_id)
#     if provider:
#         for key, value in data.items():
#             setattr(provider, key, value)
#         provider.save()
#         return jsonify(provider.to_dict())
#     else:
#         return jsonify({'error': 'Service Provider not found'}), 404
    
# # API endpoint to delete service providers
# @app.route('/api/service_providers/<int:provider_id>', methods=['DELETE'])
# def delete_service_provider(provider_id):
#     provider = Service_Providers.get_or_none(Service_Providers.OrganizationID == provider_id)
#     if provider:
#         provider.delete_instance()
#         return '', 204
#     else:
#         return jsonify({'error': 'Service Provider not found'}), 404

################ service providers above ############################


# @app.route('/api/visit_records/details', methods=['GET'])
# def get_visit_records_details():
#     query = (Visit_Record
#              .select(Visit_Record, Neighbor, Volunteer)
#              .join(Neighbor)
#              .join(Volunteer))
#     visit_records = [{
#         'Neighbor': f"{record.neighbor.FirstName} {record.neighbor.LastName}",
#         'Volunteer': f"{record.volunteer.FirstName} {record.volunteer.LastName}"
#     } for record in query]
#     return jsonify(visit_records)
