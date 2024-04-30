# This file contains validation functions for various models in the application.
# Each function takes model fields as arguments and checks for proper formatting and data integrity.
# If a field does not meet the expected criteria, a ValueError is raised with an explanation.

#TODO: implement this on main.py or app.py

def validate_service_provider(organization_name, contact_person, email, phone):
    if not 0 < len(organization_name) <= 255:
        raise ValueError("Organization name must be between 1 and 255 characters.")
    if not 0 < len(contact_person) <= 255:
        raise ValueError("Contact person name must be between 1 and 255 characters.")
    if "@" not in email or len(email) > 255:
        raise ValueError("Invalid email address.")
    if not phone.isdigit() or len(phone) > 20:
        raise ValueError("Invalid phone number. It should only contain digits and be no longer than 20 characters.")

def validate_service(service_type):
    if not 0 < len(service_type) <= 255:
        raise ValueError("Service type must be between 1 and 255 characters.")

def validate_volunteer(first_name, last_name, email, phone):
    if not 0 < len(first_name) <= 255:
        raise ValueError("First name must be between 1 and 255 characters.")
    if not 0 < len(last_name) <= 255:
        raise ValueError("Last name must be between 1 and 255 characters.")
    if "@" not in email or len(email) > 255:
        raise ValueError("Invalid email address.")
    if not phone.isdigit() or len(phone) > 20:
        raise ValueError("Invalid phone number. It should only contain digits and be no longer than 20 characters.")

def validate_neighbor(first_name, last_name, phone, email):
    if not 0 < len(first_name) <= 255:
        raise ValueError("First name must be between 1 and 255 characters.")
    if not 0 < len(last_name) <= 255:
        raise ValueError("Last name must be between 1 and 255 characters.")
    if not phone.isdigit() or len(phone) > 20:
        raise ValueError("Invalid phone number. It should only contain digits and be no longer than 20 characters.")
    if "@" not in email or len(email) > 255:
        raise ValueError("Invalid email address.")

def validate_inventory(name_of_item, description_of_item):
    if not 0 < len(name_of_item) <= 255:
        raise ValueError("Name of item must be between 1 and 255 characters.")
    if not 0 < len(description_of_item) <= 255:
        raise ValueError("Description must be between 1 and 255 characters.")
