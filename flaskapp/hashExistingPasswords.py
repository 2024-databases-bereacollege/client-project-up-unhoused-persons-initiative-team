from werkzeug.security import generate_password_hash
from models import Volunteer

# This is for a case like adding sample data to the database.

# Retrieve all volunteers from the database
volunteers = Volunteer.select()

# Update each volunteer's password to be hashed
for volunteer in volunteers:
    hashed_password = generate_password_hash(volunteer.Password)
    volunteer.Password = hashed_password
    volunteer.save()
