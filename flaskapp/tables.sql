-- https://www.postgresqltutorial.com/


-- CREATE TABLE othertable (
--     otherid integer PRIMARY KEY,
--     data varchar
-- );

-- CREATE TABLE example (
--     id serial PRIMARY KEY,
--     username varchar(32) UNIQUE,
--     description varchar(255) NOT NULL,
--     fkey_other integer REFERENCES othertable(otherid), 
--     isInt smallint NOT NULL DEFAULT(0),
--     isBool boolean
-- );

-- Service Providers
CREATE TABLE Service_Providers (
    OrganizationID VARCHAR(255) PRIMARY KEY,
    Organization_Name VARCHAR(255),
    ContactPerson VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    DateOfStart DATE
);

-- Services
CREATE TABLE Services (
    ServiceID SERIAL PRIMARY KEY,
    ServiceType VARCHAR(255),
    Organization VARCHAR(255) REFERENCES Service_Providers(OrganizationID)
);

-- Volunteer
CREATE TABLE Volunteer (

    VolunteerID SERIAL PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Password VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    HasRecordAccess BOOLEAN
);


-- Neighbor
CREATE TABLE Neighbor (
    NeighborID SERIAL PRIMARY KEY,
    VolunteerID INTEGER REFERENCES Volunteer(VolunteerID),
    OrganizationID VARCHAR(255) REFERENCES Service_Providers(OrganizationID),
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    DateOfBirth DATE,
    Phone VARCHAR(20),
    Location TEXT,
    Email VARCHAR(255),
    Created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    HasStateID BOOLEAN,
    HasPet BOOLEAN
);


-- Visit Record
CREATE TABLE Visit_Record (
    RecordID SERIAL PRIMARY KEY,
    ServiceOrder INTEGER, 
    Date DATE,
    NeighborID INTEGER REFERENCES Neighbor(NeighborID),
    VolunteerID INTEGER REFERENCES Volunteer(VolunteerID)
);

-- Visit Service
CREATE TABLE Visit_Service (
    ServiceOrder SERIAL PRIMARY KEY,
    ServiceID INTEGER REFERENCES Services(ServiceID),
    Description TEXT,
    RecordID INTEGER REFERENCES Visit_Record(RecordID)
);

-- Inventory Usage
CREATE TABLE Inventory_Usage (
    Inventory_UseID SERIAL PRIMARY KEY,
    NameOfItem VARCHAR(255),
    RecordID INTEGER REFERENCES Visit_Record(RecordID),
    Description_of_Item VARCHAR(255),
    Number_Of_Item_Used INTEGER
);

-- Inventory
CREATE TABLE Inventory (
    InventoryID SERIAL PRIMARY KEY,
    NameOfItem VARCHAR(255),
    VolunteerID INTEGER REFERENCES Volunteer(VolunteerID),
    Description_of_Item VARCHAR(255),
    ExpirationDate DATE,
    Number_Of_Item INTEGER
);


