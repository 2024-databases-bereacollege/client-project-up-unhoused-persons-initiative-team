from flask import Flask, request, redirect, render_template, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash #Using for passwords 
from models import *

#Different way of sending the information to the front end for the client to use whichever they prefer.

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r"/*": {'origins': "*"}})


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Response from root - Home page - This is being sent by backend /"})

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        
        # Hash the password for security
        hashed_password = generate_password_hash(password)

        # Check if the username already exists in the database
        existing_user = Volunteer.get_or_none(VolunteerID=username)
        if existing_user:
            # Update existing user's information
            existing_user.Email = email
            existing_user.Password = hashed_password
            existing_user.Phone = phone
            existing_user.save()  # Save the changes to the database
            return jsonify(existing_user.to_dict())
        else:
            # Create a new volunteer profile
            new_volunteer = Volunteer.create(VolunteerID=username, Email=email, Password=hashed_password, Phone=phone)
            return jsonify(new_volunteer.to_dict())

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # Extract username and password from the login form
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists in the database and if the password is correct
        user = Volunteer.get_or_none(VolunteerID=username)
        if user and check_password_hash(user.Password, password):
            # Set the user's username in the session to track their login status
            session['username'] = user.VolunteerID
            return jsonify({"message": "Login successful"})
        else:
            # Display an error message if the login credentials are invalid
            return jsonify({"error": "Invalid username or password"})

@app.route('/logout', methods=['GET'])
def logout():
    # Clear the session to log the user out
    session.clear()
    return jsonify({"message": "Logged out successfully"})


@app.route('/volunteer', methods=['GET'])
def get_volunteer():
    volunteer = [volunteer.to_dict() for volunteer in Volunteer.select()]
    return jsonify(volunteer)

@app.route('/volunteers/add', methods=['POST'])
def add_volunteer():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        
        # Hash the password for security
        hashed_password = generate_password_hash(password)

        # Check if the volunteer already exists in the database
        existing_volunteer = Volunteer.get_or_none(Email=email)
        if existing_volunteer:
            # Update existing volunteer's information
            existing_volunteer.VolunteerID = username
            existing_volunteer.Password = hashed_password
            existing_volunteer.Phone = phone
            existing_volunteer.save()  # Save the changes to the database
            return jsonify(existing_volunteer.to_dict())
        else:
            # Create a new volunteer
            new_volunteer = Volunteer.create(
                VolunteerID=username,
                Email=email,
                Password=hashed_password,
                Phone=phone
            )
            return jsonify(new_volunteer.to_dict())


@app.route('/neighbors', methods=['GET'])
def get_neighbors():
    neighbors = [neighbor.to_dict() for neighbor in Neighbor.select()]
    return jsonify(neighbors)

@app.route('/neighbors/add', methods=['POST'])
def add_neighbor():
    if request.method == 'POST':
        # Extract form data
        # Adjust this part based on your actual form structure
        first_name = request.form['FirstName']
        last_name = request.form['LastName']
        organization = request.form['Organization']
        email = request.form['Email']
        date_of_birth = request.form['DateOfBirth']
        phone = request.form['Phone']
        location = request.form['Location']
        has_pet = request.form.get('HasPet')
        has_state_id = request.form.get('HasStateID')

        # Check if the neighbor already exists in the database
        existing_neighbor = Neighbor.get_or_none(FirstName=first_name, LastName=last_name)
        if existing_neighbor:
            # Update existing neighbor's information
            existing_neighbor.OrganizationID = organization
            existing_neighbor.Email = email
            existing_neighbor.DateOfBirth = date_of_birth
            existing_neighbor.Phone = phone
            existing_neighbor.Location = location
            existing_neighbor.HasPet = has_pet
            existing_neighbor.HasStateID = has_state_id
            existing_neighbor.save()  # Save the changes to the database
            return jsonify(existing_neighbor.to_dict())
        else:
            # Create a new neighbor
            new_neighbor = Neighbor.create(
                FirstName=first_name,
                LastName=last_name,
                OrganizationID=organization,
                Email=email,
                DateOfBirth=date_of_birth,
                Phone=phone,
                Location=location,
                HasPet=has_pet,
                HasStateID=has_state_id
            )
            return jsonify(new_neighbor.to_dict())

@app.route('/providers', methods=['GET'])
def get_providers():
    providers = [provider.to_dict() for provider in Service_Providers.select()]
    return jsonify(providers)

@app.route('/providers/add', methods=['POST'])
def add_provider():
    if request.method == 'POST':
        # Extract form data
        # Adjust this part based on your actual form structure
        organization_id = request.form['OrganizationID']
        organization_name = request.form['Organization_Name']
        contact_person = request.form['ContactPerson']
        email = request.form['Email']
        phone = request.form['Phone']
        date_of_start = request.form['DateOfStart']

        # Check if the provider already exists in the database
        existing_provider = Service_Providers.get_or_none(OrganizationID=organization_id)
        if existing_provider:
            # Update existing provider's information
            existing_provider.Organization_Name = organization_name
            existing_provider.ContactPerson = contact_person
            existing_provider.Email = email
            existing_provider.Phone = phone
            existing_provider.DateOfStart = date_of_start
            existing_provider.save()  # Save the changes to the database
            return jsonify(existing_provider.to_dict())
        else:
            # Create a new service provider
            new_provider = Service_Providers.create(
                OrganizationID=organization_id,
                Organization_Name=organization_name,
                ContactPerson=contact_person,
                Email=email,
                Phone=phone,
                DateOfStart=date_of_start
            )
            return jsonify(new_provider.to_dict())

@app.route('/services', methods=['GET'])
def get_services():
    services = [service.to_dict() for service in Services.select()]
    return jsonify(services)

@app.route('/services/add', methods=['POST'])
def add_service():
    if request.method == 'POST':
        # Extract form data
        # Adjust this part based on your actual form structure
        service_type = request.form['ServiceType']
        organization_id = request.form['OrganizationID']

        # Create a new service
        new_service = Services.create(
            ServiceType=service_type,
            OrganizationID=organization_id
        )
        return jsonify(new_service.to_dict())

@app.route('/visits', methods=['GET'])
def get_visits():
    visits = [visit.to_dict() for visit in Visit_Record.select()]
    return jsonify(visits)

@app.route('/visits/add', methods=['POST'])
def add_visit():
    if request.method == 'POST':
        # Extract form data
        # Adjust this part based on your actual form structure
        date = request.form['Date']
        time = request.form['Time']
        notes = request.form['Notes']
        neighbor_id = request.form['NeighborID']
        volunteer_id = request.form['VolunteerID']

        # Create a new visit record
        new_visit = Visit_Record.create(
            Date=date,
            Time=time,
            Notes=notes,
            NeighborID=neighbor_id,
            VolunteerID=volunteer_id
        )
        return jsonify(new_visit.to_dict())

@app.route('/inventory_usage', methods=['GET'])
def get_inventory_usage():
    inventory_usage = [usage.to_dict() for usage in Inventory_Usage.select()]
    return jsonify(inventory_usage)

@app.route('/inventory_usage/add', methods=['POST'])
def add_inventory_usage():
    if request.method == 'POST':
        # Extract form data
        # Adjust this part based on your actual form structure
        name_of_item = request.form['NameOfItem']
        record_id = request.form['RecordID']
        description_of_item = request.form['Description_of_Item']
        number_of_item_used = request.form['Number_Of_Item_Used']

        # Create a new inventory usage record
        new_usage = Inventory_Usage.create(
            NameOfItem=name_of_item,
            RecordID=record_id,
            Description_of_Item=description_of_item,
            Number_Of_Item_Used=number_of_item_used
        )
        return jsonify(new_usage.to_dict())

@app.route('/inventory', methods=['GET'])
def get_inventory():
    inventory = [item.to_dict() for item in Inventory.select()]
    return jsonify(inventory)

@app.route('/inventory/add', methods=['POST'])
def add_inventory():
    if request.method == 'POST':
        # Extract form data
        # Adjust this part based on your actual form structure
        name_of_item = request.form['NameOfItem']
        volunteer_id = request.form['VolunteerID']
        description_of_item = request.form['Description_of_Item']
        expiration_date = request.form['ExpirationDate']
        number_of_item = request.form['Number_Of_Item']
        order_number = request.form['Order_Number']

        # Create a new inventory item
        new_item = Inventory.create(
            NameOfItem=name_of_item,
            VolunteerID=volunteer_id,
            Description_of_Item=description_of_item,
            ExpirationDate=expiration_date,
            Number_Of_Item=number_of_item,
            Order_Number=order_number
        )
        return jsonify(new_item.to_dict())

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
