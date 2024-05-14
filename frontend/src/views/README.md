# Creating a new visit:
Visit Date corresponds to the Date column in the Visit_Service table.
Service Name corresponds to the ServiceType column in the Services table, which is related to the Visit_Service table through the ServiceID foreign key.
Description corresponds to the Description column in the Visit_Service table.
Volunteer Name corresponds to the concatenation of FirstName and LastName columns in the Volunteer table, which is related to the Visit_Record table through the VolunteerID foreign key.
Neighbor First Name and Neighbor Last Name correspond to the FirstName and LastName columns, respectively, in the Neighbor table, which is related to the Visit_Record table through the NeighborID foreign key.
Neighbor ID corresponds to the NeighborID column in the Neighbor table.
Service Provider corresponds to the Organization_Name column in the Service_Providers table, which is related to the Services table through the OrganizationID foreign key.

When a volunteer creates a new visit log for a neighbor, they would need to provide the following information:

ServiceID: The ID of the service being provided, which is a foreign key referencing the Services table.
Description: A description of the visit or service provided.
Date: The date of the visit or service.
NeighborID: The ID of the neighbor receiving the service, which is a foreign key referencing the Neighbor table.
VolunteerID: The ID of the volunteer providing the service, which is a foreign key referencing the Volunteer table.

*This creates a new record in the Visit_Service table and a corresponding record in the Visit_Record table, which will link the visit service to the specific neighbor and volunteer.*
