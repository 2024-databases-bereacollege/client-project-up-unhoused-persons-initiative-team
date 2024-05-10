from peewee import *
from datetime import datetime 
from playhouse.shortcuts import model_to_dict # Allows us to send data as dictionaries
# Database Configuration
db = PostgresqlDatabase("db",host="localhost",user="postgres",password="postgres") #updated from mydb = PostgresqlDatabase("postgres",host="localhost",user="postgres",password="postgres") 
#Changed back to db
class baseModel(Model):
    def to_dict(self):
        return model_to_dict(self)    
    class Meta:
        database = db
class Service_Providers(baseModel):
    OrganizationID = AutoField() 
    Organization_Name = CharField(max_length=255)
    ContactPerson = CharField(max_length=255)
    Email = CharField(max_length=255)
    Phone = CharField(max_length=20)
    DateOfStart = DateField()

class Services(baseModel):
    ServiceID = AutoField() 
    ServiceType = CharField(max_length=255)
    OrganizationID = ForeignKeyField(Service_Providers, backref='services') 
    ServiceDescription = TextField() 

class Volunteer(baseModel):
    VolunteerID = AutoField() 
    FirstName = CharField(max_length=255)
    LastName = CharField(max_length=255)
    Password = CharField()
    Email = CharField(max_length=255)
    Phone = CharField(max_length=20)
    HasRecordAccess = BooleanField()

class Neighbor(baseModel):
    NeighborID = AutoField()
    FirstName = CharField(max_length=255, null=True)
    LastName = CharField(max_length=255, null=True)
    DateOfBirth = DateField(null=True, default=None)
    Phone = CharField(max_length=20, null=True)
    Location = TextField(null=True)
    Email = CharField(max_length=255, null=True)
    Created_date = DateTimeField(default=datetime.now)
    HasStateID = BooleanField(default=False)
    HasPet = BooleanField(default=False)
    HasChildren = BooleanField(default=False)
    HasMedication = BooleanField(default=False)
    HasFoodInsecurity = BooleanField(default=False)
    HasTransportation = BooleanField(default=False)
    HasJob = BooleanField(default=False)
    HasHousing = BooleanField(default=False)
    HasInsurance = BooleanField(default=False)
    HasIncome = BooleanField(default=False)
    Notes = TextField(null=True)

class Visit_Service(baseModel):
    RecordID = AutoField() 
    ServiceID = ForeignKeyField(Services, backref='visit_service')
    Description = TextField()
    Date = DateField()
class Visit_Record(baseModel):
    ServiceOrder = AutoField() 
    NeighborID = ForeignKeyField(Neighbor, backref='visit_record')  
    VolunteerID = ForeignKeyField(Volunteer, backref='visit_record')  
    RecordID = ForeignKeyField(Visit_Service, backref='visit_record') 
class Inventory_Usage(baseModel):
    Inventory_UseID = AutoField() 
    NameOfItem = CharField(max_length=255)
    RecordID = ForeignKeyField(Visit_Record, backref='Inventory_Usage')
    Description_of_Item = CharField(max_length=255)
    Number_Of_Item_Used = IntegerField()
class Inventory(baseModel):
    InventoryID = AutoField()
    NameOfItem = CharField(max_length=255)
    #VolunteerID = ForeignKeyField(Volunteer, backref='inventory')  #Taking this out, As we do not need to know what volunteer removed an item.
    Description_of_Item = CharField(max_length=255)
    ExpirationDate = DateField()
    Number_Of_Item = IntegerField()
